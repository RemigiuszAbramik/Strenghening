# Generated by Django 4.1.2 on 2022-11-07 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_profile_image_alter_profile_user'),
        ('forum', '0006_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.profile'),
        ),
    ]
