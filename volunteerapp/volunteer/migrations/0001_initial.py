# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(help_text='Please add a descriptive name.', blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(help_text='The slug field is automatically set, based on the shift name.')),
                ('description', models.TextField(help_text='Describe the shift.', blank=True, max_length=100, null=True)),
                ('status', models.CharField(help_text='Status of the item (e.g. draft, active or closed. Draft is default.', blank=True, max_length=2, default='DR', null=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(help_text='Please add a descriptive name.', blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(help_text='The slug field is automatically set, based on the shift name.')),
                ('description', models.TextField(help_text='Describe the shift.', blank=True, max_length=100, null=True)),
                ('status', models.CharField(help_text='Status of the item (e.g. draft, active or closed. Draft is default.', blank=True, max_length=2, default='DR', null=True)),
                ('event', models.ManyToManyField(blank=True, to='volunteer.Event', null=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', default=django.utils.timezone.now, editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(help_text='Please add a descriptive name.', blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(help_text='The slug field is automatically set, based on the shift name.')),
                ('description', models.TextField(help_text='Describe the shift.', blank=True, max_length=100, null=True)),
                ('status', models.CharField(help_text='Status of the item (e.g. draft, active or closed. Draft is default.', blank=True, max_length=2, default='DR', null=True)),
                ('max_volunteers', models.PositiveIntegerField(help_text='Number of volunteers are needed for this shift', blank=True, null=True)),
                ('start_datetime', models.TimeField(help_text='Shift start date and time')),
                ('end_datetime', models.TimeField(help_text='Shift end date and time')),
                ('volunteers', models.ManyToManyField(help_text='Project-Id-Version: Django\nReport-Msgid-Bugs-To: \nPOT-Creation-Date: 2013-05-02 16:18+0200\nPO-Revision-Date: 2010-05-13 15:35+0200\nLast-Translator: Django team\nLanguage-Team: English <en@li.org>\nLanguage: en\nMIME-Version: 1.0\nContent-Type: text/plain; charset=UTF-8\nContent-Transfer-Encoding: 8bit\n', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['start_datetime'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='session',
            field=models.ManyToManyField(blank=True, to='volunteer.Shift', null=True),
            preserve_default=True,
        ),
    ]
