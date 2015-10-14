# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fgfw', '0003_remove_youtubeurl_test_mod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubeurl',
            name='request_url',
            field=models.URLField(),
        ),
    ]
