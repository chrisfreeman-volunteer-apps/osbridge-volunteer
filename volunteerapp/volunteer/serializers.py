from rest_framework import serializers
from .models import Organization, Event, Shift


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = (
            'id', 'name', 'slug', 'status', 'get_status_display',
            'description', 'location', 'get_num_events',
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id', 'name', 'slug', 'status', 'description', 'location', 'session',
        )


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = (
            'id', 'name', 'slug', 'status', 'description', 'location',
            'max_volunteers', 'start_datetime', 'end_datetime',
            'is_full', 'get_num_volunteers', 'get_duration',
            'get_percent_full', 'get_remaining_space',
        )
