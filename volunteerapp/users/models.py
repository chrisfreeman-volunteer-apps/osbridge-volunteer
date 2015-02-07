# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Subclass AbstractUser
class Users(AbstractUser):

    SIZE_CHOICES = (
        ('--', _('Choose Shirt Size')),
        ('NA', _('I Do Not Want a Shirt')),
        ('MS', _('Men Small')),
        ('MM', _('Men Medium')),
        ('ML', _('Men Large')),
        ('MXL', _('Men XL')),
        ('M2X', _('Men 2XL')),
        ('WS', _('Women Small')),
        ('WM', _('Women Medium')),
        ('WL', _('Women Large')),
        ('WXL', _('Women XL')),
        ('W2X', _('Women 2XL')),
    )

    middle_initial = models.CharField(
        max_length=3, null=True, blank=True)
    profile_image = models.ImageField(
        upload_to='../media/participants', null=True, blank=True)
    phone = models.CharField(
        max_length=20, null=True, blank=True)
    dietary = models.TextField(
        null=True, blank=True,
        help_text=_(
            "Do you have any dietary restrictions (vegan/vegetarian) " +
            "or food allergies (gluten free, etc.). Please be specific."))
    shirt_size = models.TextField(
        null=True, blank=True,
        help_text=_("What's your T-Shirt size?"))

    class Meta:
        ordering = ['last_name', 'first_name']

    def __unicode__(self):
        return self.username

    def short_name(self):
        '''
        Returns first and last name of the user's profile.
        '''
        return '%s %s' % (self.first_name, self.last_name)

    def full_name(self):
        '''
        The first name, middle initial and last name of the participant,
        if middle initial is saved.
        '''
        if self.middle_initial:
            return '%s %s. %s' % (self.first_name, self.middle_initial, self.last_name)
        return self.short_name(self)
