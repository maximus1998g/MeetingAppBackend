# Generated by Django 3.0.3 on 2020-11-12 10:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0006_auto_20201112_1006'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lastseenmessage',
            unique_together={('chat_id', 'user')},
        ),
    ]
