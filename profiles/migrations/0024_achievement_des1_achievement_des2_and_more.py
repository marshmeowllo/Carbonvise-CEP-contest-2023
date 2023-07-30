# Generated by Django 4.2.2 on 2023-07-29 17:14

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='des1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='achievement',
            name='des2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='achievement',
            name='image_compare',
            field=models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_path),
        ),
    ]
