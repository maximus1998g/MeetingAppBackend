# Generated by Django 3.0.3 on 2020-06-10 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20200610_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='categories',
        ),
    ]
