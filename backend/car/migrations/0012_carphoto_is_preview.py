# Generated by Django 4.2 on 2024-05-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0011_car_daily_rent_car_price_car_short_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carphoto',
            name='is_preview',
            field=models.BooleanField(default=False),
        ),
    ]
