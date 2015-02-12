# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0009_auto_20150129_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(help_text='Please add a descriptive name for             thisjob/category or restriction.', max_length=100, unique=True, null=True)),
                ('description', models.TextField(help_text='Describe this job/category or restriction.', null=True, blank=True)),
                ('slug', models.SlugField(help_text='The slug field is automatically set.', max_length=100, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(help_text='Please add a descriptive name for             thisjob/category or restriction.', max_length=100, unique=True, null=True)),
                ('description', models.TextField(help_text='Describe this job/category or restriction.', null=True, blank=True)),
                ('slug', models.SlugField(help_text='The slug field is automatically set.', max_length=100, blank=True)),
                ('organization', models.ForeignKey(blank=True, to='volunteer.Organization', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobRestriction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(help_text='Please add a descriptive name for             thisjob/category or restriction.', max_length=100, unique=True, null=True)),
                ('description', models.TextField(help_text='Describe this job/category or restriction.', null=True, blank=True)),
                ('slug', models.SlugField(help_text='The slug field is automatically set.', max_length=100, blank=True)),
                ('organization', models.ForeignKey(blank=True, to='volunteer.Organization', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(blank=True, to='volunteer.JobCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='organization',
            field=models.ForeignKey(blank=True, to='volunteer.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='restriction',
            field=models.ForeignKey(blank=True, to='volunteer.JobRestriction', null=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='event',
            name='session',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='organization',
            field=models.ForeignKey(blank=True, to='volunteer.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shift',
            name='event',
            field=models.ForeignKey(blank=True, to='volunteer.Event', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shift',
            name='job',
            field=models.ForeignKey(blank=True, to='volunteer.Job', help_text='What duties need to be performed during this shift?', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(help_text='Describe the shift.', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.TextField(help_text='Where is the organization, event or shift located or held?', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(help_text='The slug field is automatically set, based on the shift name.', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.TextField(help_text='Describe the shift.', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='location',
            field=models.TextField(help_text='Where is the organization, event or shift located or held?', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=models.SlugField(help_text='The slug field is automatically set, based on the shift name.', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shift',
            name='description',
            field=models.TextField(help_text='Describe the shift.', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shift',
            name='location',
            field=models.TextField(help_text='Where is the organization, event or shift located or held?', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shift',
            name='slug',
            field=models.SlugField(help_text='The slug field is automatically set, based on the shift name.', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='checked_out_statement',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'-', 'Choose the Status'), (b'O', 'Outstanding Volunteer'), (b'A', 'Amazing Help'), (b'G', 'Great Support'), (b'N', 'Not sure if I would recommend')]),
            preserve_default=True,
        ),
    ]
