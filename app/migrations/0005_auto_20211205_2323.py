# Generated by Django 3.2.9 on 2021-12-05 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_image_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='postee',
        ),
        migrations.RemoveField(
            model_name='image',
            name='postee',
        ),
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
    ]
