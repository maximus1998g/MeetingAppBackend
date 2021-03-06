# Generated by Django 3.0.3 on 2020-06-10 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('tickets', '0004_remove_ticket_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.SubCategory')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket')),
            ],
            options={
                'db_table': 'ticket_categories',
                'unique_together': {('ticket', 'category')},
            },
        ),
    ]
