# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 11:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busshaming', '0004_auto_20170812_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='route_color',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='route_desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='route_long_name',
            new_name='long_name',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='route_short_name',
            new_name='short_name',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='route_text_color',
            new_name='text_color',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='route_url',
            new_name='url',
        ),
    ]