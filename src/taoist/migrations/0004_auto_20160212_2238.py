# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taoist', '0003_auto_20160212_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videourl',
            name='time_finish_download',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videourl',
            name='time_finish_upload',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videourl',
            name='time_start_download',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videourl',
            name='time_start_upload',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
