# Generated by Django 4.2 on 2024-05-15 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_rent_invest', '0010_alter_userrent_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinvestment',
            name='investment',
        ),
        migrations.RemoveField(
            model_name='userinvestment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Investment',
        ),
        migrations.DeleteModel(
            name='UserInvestment',
        ),
    ]
