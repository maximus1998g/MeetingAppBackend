# Generated by Django 3.0.3 on 2020-11-12 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20201112_1335'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lastseenmessage',
            unique_together=set(),
        ),
    ]
