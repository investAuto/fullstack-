# Generated by Django 4.2 on 2024-05-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0022_alter_technicalservice_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carvideo',
            name='video',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='Видео'),
        ),
    ]