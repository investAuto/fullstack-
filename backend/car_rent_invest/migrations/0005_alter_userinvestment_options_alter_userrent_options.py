# Generated by Django 4.2 on 2024-05-08 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_rent_invest', '0004_alter_userrent_options_alter_rent_daily_cost_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinvestment',
            options={'default_related_name': 'user_investment',
                     'verbose_name': 'Инвестиция', 'verbose_name_plural': 'Инвестиции'},
        ),
        migrations.AlterModelOptions(
            name='userrent',
            options={'default_related_name': 'user_rent',
                     'verbose_name': 'Аренда', 'verbose_name_plural': 'Аренды'},
        ),
    ]
