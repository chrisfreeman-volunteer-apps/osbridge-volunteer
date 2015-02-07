from rest_framework import viewsets, permissions

from .models import Organization, Event, Shift
from .serializers import OrganizationSerializer, EventSerializer, ShiftSerializer
from .permissions import IsObjectAdminOrReadOnly


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsObjectAdminOrReadOnly,
    )
    lookup_field = 'slug'

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.admin.add(self.request.user)


class EventViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsObjectAdminOrReadOnly,
    )
    lookup_field = 'slug'

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.admin.add(self.request.user)


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
