# Generated by Django 4.2 on 2024-05-15 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0018_alter_car_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartechnicalservice',
            options={'default_related_name': 'car_technical_services', 'verbose_name': 'Обслуживание', 'verbose_name_plural': 'Обслуживания'},
        ),
    ]
