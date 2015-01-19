# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .models import Users


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Users


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Users.objects.get(username=username)
        except Users.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class UserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('username', 'first_name', 'last_name', 'is_active')
    list_editable = ('is_active',)


admin.site.register(Users, UserAdmin)



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
