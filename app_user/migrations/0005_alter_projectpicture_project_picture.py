# Generated by Django 3.2.16 on 2023-03-11 16:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_user", "0004_remove_user_follows"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectpicture",
            name="project_picture",
            field=cloudinary.models.CloudinaryField(
                max_length=255, verbose_name="project_picture"
            ),
        ),
    ]
