# Generated by Django 4.2 on 2024-05-13 06:53

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0010_auto_20240508_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='daily_rent',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1000)], verbose_name='Стоимость аренды в день'),
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(10000000), django.core.validators.MinValueValidator(100000)], verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='car',
            name='short_description',
            field=models.CharField(max_length=256, null=True, verbose_name='Короткое описание на главной'),
        ),
        migrations.AlterField(
            model_name='car',
            name='technical_service',
            field=models.ManyToManyField(help_text='Удерживайте Ctrl для выбора нескольких вариантов', through='car.CarTechnicalService', to='car.technicalservice', verbose_name='Обслуживания'),
        ),
        migrations.AlterField(
            model_name='carphoto',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car'),
        ),
        migrations.AlterField(
            model_name='carvideo',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car'),
        ),
    ]
