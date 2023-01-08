# Generated by Django 4.1.2 on 2022-12-09 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_profile_image_alter_profile_user'),
        ('training', '0003_alter_training_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.FloatField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.profile')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.training')),
            ],
        ),
    ]