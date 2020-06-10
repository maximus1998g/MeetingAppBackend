from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from common.serializers import SubCategorySerializer
from common.utils import set_event_categories, set_geo_point
from token_auth.serializers import UserProfileSerializer
from .models import Event, Request, GeoPoint


class GeoPointSerializer(ModelSerializer):
    class Meta:
        model = GeoPoint
        fields = ('address', 'longitude', 'latitude')


class EventSerializer(ModelSerializer):
    id = serializers.ReadOnlyField()
    creator = UserProfileSerializer(read_only=True)
    categories = SubCategorySerializer(many=True, read_only=True, required=False)
    members = UserProfileSerializer(read_only=True, many=True)
    geo_point = GeoPointSerializer()

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        geo_point_validated = validated_data.pop('geo_point')
        geo_point = GeoPoint.objects.create(**geo_point_validated)
        event = Event.objects.create(geo_point=geo_point, **validated_data)

        categories = validated_data.pop('categories')
        if categories is not None:
            set_event_categories(categories, instance)

        return event

    def update(self, instance, validated_data):
        instance.description = validated_data.pop('description')
        instance.date = validated_data.pop('date')
        instance.time = validated_data.get('time', instance.time)
        instance.save()

        categories = validated_data.pop('categories')
        if categories is not None:
            set_event_categories(categories, instance)

        set_geo_point(instance.geo_point, validated_data)

        return instance


class RequestSerializer(ModelSerializer):
    to_user = UserProfileSerializer(read_only=True)
    event = serializers.IntegerField(source='event.id', read_only=True)
    from_user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Request
        fields = '__all__'
        extra_kwargs = {'decision': {'required': False}}
