from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import ComplaintListView, ComplaintDetailView, UserProfileWarningListView, UserProfileWarningDetailView

urlpatterns = [
    path('complaints/', csrf_exempt(ComplaintListView.as_view())),
    path('complaints/<int:pk>/', csrf_exempt(ComplaintDetailView.as_view())),

    path('warnings/', csrf_exempt(UserProfileWarningListView.as_view())),
    path('warnings/<int:pk>/', csrf_exempt(UserProfileWarningDetailView.as_view())),
]
