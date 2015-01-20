# -*- coding: utf-8 -*-
# Python methods and packages
from decimal import Decimal
# from datetime import datetime, timedelta

# Django packages
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

# 3rd party package
from model_utils.models import TimeStampedModel

# app models
from users.models import Users


class CommonModel(TimeStampedModel):

    STATUS_CHOICES = (
        ('--', _('Choose the Status')),
        ('AA', _('Active')),
        ('DR', _('Draft Mode')),
        ('CL', _('Closed')),
    )

    name = models.CharField(
        max_length=100, null=True,
        help_text=_("Please add a descriptive name."))
    slug = models.SlugField(
        max_length=50, blank=True,
        help_text=_("The slug field is automatically set, based on the shift name."))
    description = models.TextField(
        max_length=100, null=True, blank=True,
        help_text=_("Describe the shift."))
    status = models.CharField(
        max_length=2, default='DR', choices=STATUS_CHOICES,
        help_text=_("Status of the item (e.g. draft, active or closed). Draft is default."))

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def clean_name(self):
        name = self.cleaned_data["name"]
        try:
            self.__class__.objects.get(name=name)
        except self.__class__.DoesNotExist:
            return name
        return name
        # raise forms.ValidationError(self.error_messages['duplicate_name'])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CommonModel, self).save(*args, **kwargs)


class Shift(CommonModel):

    max_volunteers = models.PositiveIntegerField(
        blank=True, null=True,
        help_text=_("Number of volunteers are needed for this shift"))
    volunteers = models.ManyToManyField(
        Users, null=True, blank=True,
        help_text=_("Lists all registered volunteers for this shift."))
    start_datetime = models.DateTimeField(
        null=True, blank=True,
        help_text=_("Shift start date and time"))
    end_datetime = models.DateTimeField(
        null=True, blank=True,
        help_text=_("Shift end date and time"))

    class Meta:
        ordering = ['start_datetime']

    def __str__(self):
        return self.name

    def is_full(self):
        if self.max_volunteers is None:
            return False
        if self.volunteers.count() < self.max_volunteers:
            return False
        else:
            return True

    def get_remaining_space(self):
        if self.max_volunteers is None:
            return unicode('unlimited')
        space = self.max_volunteers - self.volunteers.count()
        if space < 0:
            space = 0
        return space

    def get_percent_full(self):
        if self.max_volunteers is None:
            percent = Decimal('0.00')
        else:
            try:
                percent = Decimal(
                    self.volunteers.count()) / Decimal(self.max_volunteers) * Decimal(100)
            except:
                percent = Decimal('0.00')

        if percent > 100:
            percent = 100
        return percent.quantize(Decimal('1'))

    def get_num_volunteers(self):
        return self.volunteers.count()

    def get_num_hours(self):
        return self.volunteers.count() * self.get_duration()()

    def get_max_hours(self):
        if self.max_volunteers is None:
            return Decimal('0.00')
        return self.max_volunteers * self.get_duration()

    def get_duration(self):
        # difference is in seconds (float with milli seconds)
        # methods returns difference in Hours (as float)
        difference = self.end_datetime - self.start_datetime
        return round(difference.total_seconds() / 60 / 60, 2)


class Event(CommonModel):

    session = models.ManyToManyField(
        Shift, null=True, blank=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name

    def get_num_shifts(self):
        '''
        Returns the total number of registered sesssions
        '''
        return self.session.count()


class Organization(CommonModel):

    event = models.ManyToManyField(
        Event, null=True, blank=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name

    def get_num_events(self):
        '''
        Returns the total number of registered events
        '''
        return self.event.count()
