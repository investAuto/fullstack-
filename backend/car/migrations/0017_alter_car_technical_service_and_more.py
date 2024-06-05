# Generated by Django 4.2 on 2024-05-14 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0016_alter_car_technical_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='technical_service',
            field=models.ManyToManyField(help_text='Удерживайте Ctrl для выбора нескольких вариантов', through='car.CarTechnicalService', to='car.technicalservice', verbose_name='Обслуживания'),
        ),
        migrations.AlterField(
            model_name='cartechnicalservice',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car.car', verbose_name='Автомобиль'),
        ),
    ]