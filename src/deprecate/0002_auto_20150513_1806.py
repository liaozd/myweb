# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fgfw', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtubeurl',
            name='timestamp2',
        ),
        migrations.RemoveField(
            model_name='youtubeurl',
            name='timestamp3',
        ),
    ]
