# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('volunteer', '0004_auto_20150120_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('checked_in_datetime', models.DateTimeField(blank=True, null=True)),
                ('checked_out_datetime', models.DateTimeField(blank=True, null=True)),
                ('marked_noshow_at', models.DateTimeField(blank=True, null=True)),
                ('marked_canceled_datetime', models.DateTimeField(blank=True, null=True)),
                ('checked_in_by', models.ForeignKey(related_name='volunteer_checked_in_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('checked_out_by', models.ForeignKey(related_name='volunteer_checked_out_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('marked_canceled_by', models.ForeignKey(related_name='volunteer_marked_canceled_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('marked_noshow_by', models.ForeignKey(related_name='volunteer_marked_noshow_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('shift', models.ForeignKey(to='volunteer.Shift', help_text='Which shift will the volunteer cover?')),
                ('volunteer', models.ForeignKey(to=settings.AUTH_USER_MODEL, help_text='Who is the volunteer?')),
            ],
            options={
                'ordering': ['shift__start_datetime'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=100, help_text='Please add a descriptive name.', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=100, help_text='Please add a descriptive name.', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shift',
            name='name',
            field=models.CharField(max_length=100, help_text='Please add a descriptive name.', null=True),
            preserve_default=True,
        ),
    ]
