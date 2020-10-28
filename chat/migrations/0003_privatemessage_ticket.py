# Generated by Django 3.0.3 on 2020-10-22 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_ticket_categories'),
        ('chat', '0002_auto_20200531_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatemessage',
            name='ticket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='tickets.Ticket'),
            preserve_default=False,
        ),
    ]
