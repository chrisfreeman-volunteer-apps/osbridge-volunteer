from rest_framework import viewsets

from .models import Organization, Event, Shift
from .serializers import OrganizationSerializer, EventSerializer, ShiftSerializer


class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    lookup_field = 'slug'


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'slug'


class ShiftViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    lookup_field = 'pk'  # pk here due to uniqueness
