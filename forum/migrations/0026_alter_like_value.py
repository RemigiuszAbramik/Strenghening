# Generated by Django 4.1.2 on 2022-12-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0025_alter_like_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10),
        ),
    ]