# Generated by Django 3.0.3 on 2020-05-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_ticket_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='place',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='row',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='zone',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
