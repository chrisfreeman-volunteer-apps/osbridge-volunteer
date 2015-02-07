# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0002_auto_20150120_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shift',
            options={'ordering': ['start_datetime']},
        ),
        migrations.AddField(
            model_name='shift',
            name='end_datetime',
            field=models.DateTimeField(blank=True, null=True, help_text='Shift end date and time'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shift',
            name='start_datetime',
            field=models.DateTimeField(blank=True, null=True, help_text='Shift start date and time'),
            preserve_default=True,
        ),
    ]
