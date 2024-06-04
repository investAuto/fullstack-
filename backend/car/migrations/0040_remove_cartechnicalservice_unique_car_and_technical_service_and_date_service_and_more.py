# Generated by Django 4.2 on 2024-05-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0039_alter_cartechnicalservice_date_service'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='cartechnicalservice',
            name='unique_car_and_technical_service_and_date_service',
        ),
        migrations.AlterField(
            model_name='cartechnicalservice',
            name='date_service',
            field=models.DateField(null=True, verbose_name='Дата технического обслуживания.'),
        ),
        migrations.AddConstraint(
            model_name='cartechnicalservice',
            constraint=models.UniqueConstraint(fields=('car', 'technical_service', 'scheduled_date'), name='unique_car_and_technical_service_and_date_service'),
        ),
    ]
