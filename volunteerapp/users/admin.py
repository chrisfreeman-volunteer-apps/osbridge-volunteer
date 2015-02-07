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
