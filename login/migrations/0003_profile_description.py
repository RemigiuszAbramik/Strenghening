# Generated by Django 4.1.2 on 2022-12-09 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_profile_image_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default="You didn't change your description yet!", max_length=1000),
        ),
    ]