# -*- coding: utf-8 -*-
from django import forms

from .models import Users


class UserForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = Users

        # Constrain the UserForm to just these fields.
        fields = ("first_name", "last_name")
