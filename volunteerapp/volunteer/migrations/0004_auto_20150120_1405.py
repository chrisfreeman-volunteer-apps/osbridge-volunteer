# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0003_auto_20150120_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(default='DR', max_length=2, help_text='Status of the item (e.g. draft, active or closed). Draft is default.', choices=[('--', 'Choose the Status'), ('AA', 'Active'), ('DR', 'Draft Mode'), ('CL', 'Closed')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='status',
            field=models.CharField(default='DR', max_length=2, help_text='Status of the item (e.g. draft, active or closed). Draft is default.', choices=[('--', 'Choose the Status'), ('AA', 'Active'), ('DR', 'Draft Mode'), ('CL', 'Closed')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shift',
            name='status',
            field=models.CharField(default='DR', max_length=2, help_text='Status of the item (e.g. draft, active or closed). Draft is default.', choices=[('--', 'Choose the Status'), ('AA', 'Active'), ('DR', 'Draft Mode'), ('CL', 'Closed')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shift',
            name='volunteers',
            field=models.ManyToManyField(null=True, help_text='Lists all registered volunteers for this shift.', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
