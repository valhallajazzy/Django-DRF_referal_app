# Generated by Django 5.0.4 on 2024-04-22 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=12, verbose_name='Номер телефона'),
        ),
    ]
