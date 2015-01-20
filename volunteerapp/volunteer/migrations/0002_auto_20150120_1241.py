# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shift',
            options={},
        ),
        migrations.RemoveField(
            model_name='shift',
            name='end_datetime',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='start_datetime',
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(help_text='The slug field is automatically set, based on the shift name.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=models.SlugField(help_text='The slug field is automatically set, based on the shift name.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shift',
            name='slug',
            field=models.SlugField(help_text='The slug field is automatically set, based on the shift name.', blank=True),
            preserve_default=True,
        ),
    ]
