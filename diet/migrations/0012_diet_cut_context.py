# Generated by Django 4.1.2 on 2022-12-12 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0011_alter_review_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet',
            name='cut_context',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]