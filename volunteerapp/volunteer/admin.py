# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Shift, Event, Organization


class CommonAdmin(admin.ModelAdmin):
    ordering = ['name', 'status']
    list_display = ('name', 'description', 'status')
    list_editable = ('status',)
    list_filter = ['status']

    class Meta:
        # model = Topic
        abstract = True


class ShiftAdmin(CommonAdmin):
    # list_display = (
        # 'num_volunteers', 'max_volunteers', 'start_datetime',
        # 'get_duration'
    # )
    # list_editable = ('max_volunteers',)
    pass


class EventAdmin(CommonAdmin):
    pass


class OrganizationAdmin(CommonAdmin):
    pass

admin.site.register(Shift, ShiftAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Organization, OrganizationAdmin)



# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# from django.contrib.auth.models import User
# from User.models import OSBProfile
# from teams.models import PDXSWTeam

# class ProfileInline(admin.StackedInline):
#     model = OSBProfile
#     fk_name = 'user'
#     max_num = 1
    #raw_id_fields = ['last_name', 'first_name', 'email']

# class TeamInline(admin.StackedInline):
#     model = PDXSWTeam
#     fk_name = 'team_user'
#     filter_horizontal = ('team_members',)
#     max_num = 1


# # class PDXSWProfileAdmin(admin.ModelAdmin):
# #     list_display = ('__unicode__')

# class OSBProfileAdmin(admin.ModelAdmin):
#     list_display = ('__unicode__', 'user', 'hours', 'shirt_size', 'status', 'phone', 'intent')
#     list_editable = ('intent',)


# class CustomUserAdmin(UserAdmin):
#     inlines = [ProfileInline, ]
#     list_display = ('username', 'last_name', 'first_name', 'email',
    # 'get_cell_phone', 'get_intent', 'get_shirt_size', 'get_status', 'is_staff', 'is_superuser')

#     def get_shirt_size(self, user):
#         return user.get_profile().shirt_size

#     def get_cell_phone(self, user):
#         return user.get_profile().phone

#     def get_status(self, user):
#         return user.get_profile().status

#     def get_intent(self, user):
#         return user.get_profile().intent


# admin.site.register(OSBProfile, OSBProfileAdmin)
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
