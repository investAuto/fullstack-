# Generated by Django 4.2 on 2024-05-16 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0025_alter_carcard_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='technical_characteristic',
            field=models.TextField(blank=True, verbose_name='Технические характеристики'),
        ),
    ]