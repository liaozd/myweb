# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taoist', '0002_videourl_time_start_download'),
    ]

    operations = [
        migrations.AddField(
            model_name='videourl',
            name='time_finish_download',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='videourl',
            name='time_finish_upload',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='videourl',
            name='time_start_upload',
            field=models.DateTimeField(null=True),
        ),
    ]
