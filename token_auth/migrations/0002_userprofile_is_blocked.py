# Generated by Django 3.0.3 on 2020-06-02 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
    ]
