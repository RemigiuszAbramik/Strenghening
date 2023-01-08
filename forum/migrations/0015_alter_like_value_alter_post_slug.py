# Generated by Django 4.1.2 on 2022-11-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0014_post_slug_alter_like_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Unlike', 'Unlike'), ('Like', 'Like')], default='Like', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]