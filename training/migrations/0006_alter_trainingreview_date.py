# Generated by Django 4.1.2 on 2022-12-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_training_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingreview',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
