# Generated by Django 2.2.24 on 2022-01-07 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_phone_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='user',
        ),
    ]
