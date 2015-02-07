# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0008_auto_20150125_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(help_text='Please add a descriptive name.', max_length=100, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(help_text='Please add a descriptive name.', max_length=100, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shift',
            name='name',
            field=models.CharField(help_text='Please add a descriptive name.', max_length=100, unique=True, null=True),
            preserve_default=True,
        ),
    ]
