# Generated by Django 5.0.4 on 2024-04-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0002_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
