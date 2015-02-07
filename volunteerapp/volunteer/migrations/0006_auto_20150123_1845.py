# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0005_auto_20150122_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.TextField(max_length=150, null=True, help_text='Where is the organization, event or shift located or held?', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='location',
            field=models.TextField(max_length=150, null=True, help_text='Where is the organization, event or shift located or held?', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shift',
            name='location',
            field=models.TextField(max_length=150, null=True, help_text='Where is the organization, event or shift located or held?', blank=True),
            preserve_default=True,
        ),
    ]
