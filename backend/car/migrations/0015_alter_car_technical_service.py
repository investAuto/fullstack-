# Generated by Django 4.2 on 2024-05-14 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0014_cartechnicalservice_unique_car_and_technical_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='technical_service',
            field=models.ManyToManyField(blank=True, help_text='Удерживайте Ctrl для выбора нескольких вариантов', through='car.CarTechnicalService', to='car.technicalservice', verbose_name='Обслуживания'),
        ),
    ]