# Generated by Django 4.2 on 2024-05-20 14:36

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0029_technicalservice_periodicity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartechnicalservice',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарий к обслуживанию.'),
        ),
        migrations.AlterField(
            model_name='technicalservice',
            name='periodicity',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(1)], verbose_name='Периодичность обслуживания, дней'),
        ),
        migrations.AlterField(
            model_name='technicalservicephoto',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='car.cartechnicalservice'),
        ),
    ]
