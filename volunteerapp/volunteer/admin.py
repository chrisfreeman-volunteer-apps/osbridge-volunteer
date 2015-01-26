# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Task, Shift, Event, Organization


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
        # 'admin',
        'get_num_shifts',
    )
    # list_editable = CommonAdmin.list_editable + ('admin',)


class OrganizationAdmin(CommonAdmin):
    list_display = CommonAdmin.list_display + (
        # 'admin',
        'get_num_events',
    )
    # list_editable = CommonAdmin.list_editable + ('admin',)


class TaskAdmin(admin.ModelAdmin):
    ordering = ['shift__name', 'shift__status']
    list_display = (
        # 'shift__name', 'shift__description',
        # 'shift__status',
        'shift', 'volunteer',
        'checked_in_by', 'marked_noshow_by')
    list_editable = ('checked_in_by', 'marked_noshow_by')
    list_filter = ['shift__status']


admin.site.register(Shift, ShiftAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Task, TaskAdmin)
