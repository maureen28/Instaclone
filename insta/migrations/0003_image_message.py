# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-31 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20200531_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='message',
            field=models.CharField(default='Hey', max_length=80),
        ),
    ]
