from rest_framework import viewsets, permissions

from .models import Organization, Event, Shift
from .serializers import OrganizationSerializer, EventSerializer, ShiftSerializer
from .permissions import IsAdminOrReadOnly


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly)
    lookup_field = 'slug'


class EventViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly)
    lookup_field = 'slug'


class ShiftViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    lookup_field = 'pk'  # pk here due to uniqueness
