# Generated by Django 4.1.2 on 2022-12-11 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_trainingreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]