from rest_framework import serializers
from .models import Users
from volunteer.models import Organization, Event, Task


class UserSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(many=True, queryset=Organization.objects.all())
    event = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())
    task = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = Users
        fields = (
            'id', 'username', 'first_name', 'last_name',
            'organization', 'event', 'task'
        )
