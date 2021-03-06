# Generated by Django 3.0.3 on 2020-06-10 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('tickets', '0005_ticketcategories'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='categories',
            field=models.ManyToManyField(through='tickets.TicketCategories', to='common.SubCategory'),
        ),
    ]
