# Generated by Django 4.2 on 2024-05-21 12:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0030_cartechnicalservice_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year_release',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(2050), django.core.validators.MinValueValidator(1900)], verbose_name='Год выпуска'),
        ),
        migrations.AlterField(
            model_name='cartechnicalservice',
            name='complited',
            field=models.BooleanField(verbose_name='Завершено'),
        ),
        migrations.AlterField(
            model_name='cartechnicalservice',
            name='date_service',
            field=models.DateField(verbose_name='Дата технического обслуживания.'),
        ),
        migrations.AddConstraint(
            model_name='cartechnicalservice',
            constraint=models.UniqueConstraint(fields=('car', 'technical_service', 'date_service'), name='unique_car_and_technical_service_and_date_service'),
        ),
    ]