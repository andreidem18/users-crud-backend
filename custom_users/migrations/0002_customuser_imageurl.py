# Generated by Django 2.2.24 on 2023-03-31 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='imageUrl',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]