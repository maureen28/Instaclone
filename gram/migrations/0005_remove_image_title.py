# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-30 19:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0004_auto_20200530_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
    ]