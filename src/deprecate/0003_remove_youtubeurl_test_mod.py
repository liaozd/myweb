# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fgfw', '0002_auto_20150513_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtubeurl',
            name='test_mod',
        ),
    ]
