# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-31 20:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_owner',
            new_name='comment_title',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='pic',
            new_name='my_image',
        ),
        migrations.RenameField(
            model_name='likes',
            old_name='liker',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='owner',
            new_name='user',
        ),
        migrations.AddField(
            model_name='image',
            name='time_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
