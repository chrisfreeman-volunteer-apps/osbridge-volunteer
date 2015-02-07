# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0007_auto_20150125_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='checked_out_statement',
            field=models.CharField(blank=True, max_length=1, choices=[('--', 'Choose the Status'), ('O', 'Outstanding Volunteer'), ('A', 'Amazing Help'), ('G', 'Great Support'), ('N', 'Not sure if I would recommend')], null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='admin',
            field=models.ManyToManyField(related_name='event', to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='admin',
            field=models.ManyToManyField(related_name='organization', to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='volunteer',
            field=models.ForeignKey(related_name='task', to=settings.AUTH_USER_MODEL, help_text='Who is the volunteer?'),
            preserve_default=True,
        ),
    ]
