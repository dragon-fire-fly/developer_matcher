# Generated by Django 3.2.16 on 2023-01-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='github_url',
            field=models.CharField(default='None', help_text='What is your GitHub URL?', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='github_user',
            field=models.CharField(default='None', help_text='What is your GitHub username?', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='linked_in',
            field=models.CharField(default='None', help_text='What is the URL of your linkedin profile?', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(default='None', help_text='Where do you live?', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='portfolio',
            field=models.CharField(default='None', help_text='What is your portfolio URL?', max_length=255),
            preserve_default=False,
        ),
    ]
