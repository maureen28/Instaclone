# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-30 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0011_remove_image_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='message',
            field=models.TextField(default='Hey there.'),
        ),
    ]
