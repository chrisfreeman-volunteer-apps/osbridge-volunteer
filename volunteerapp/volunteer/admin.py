# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Shift, Event, Organization


class CommonAdmin(admin.ModelAdmin):
    ordering = ['name', 'status']
    list_display = ('name', 'description', 'status')
    list_editable = ('status',)
    list_filter = ['status']

    class Meta:
        abstract = True


class ShiftAdmin(CommonAdmin):
    list_display = CommonAdmin.list_display + (
        'get_num_volunteers', 'max_volunteers',
        'start_datetime', 'get_duration'
    )
    list_editable = ('max_volunteers',)


class EventAdmin(CommonAdmin):
    list_display = CommonAdmin.list_display + (
        'get_num_shifts',
    )


class OrganizationAdmin(CommonAdmin):
    list_display = CommonAdmin.list_display + (
        'get_num_events',
    )

admin.site.register(Shift, ShiftAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Organization, OrganizationAdmin)
