# Generated by Django 4.1.2 on 2022-11-06 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_training_author_training_date_training_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='image',
            field=models.ImageField(default='training_pics/default.png', upload_to='diet_pics'),
        ),
    ]