# -*- coding: utf-8 -*-

# view imports
from django.views.generic import DetailView

# Only authenticated users can access views using this.
from braces.views import JSONResponseMixin
from rest_framework import viewsets, permissions

# Import the customized User model
from .models import Users
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )
    lookup_field = 'username'


class UsernameAJAXView(JSONResponseMixin, DetailView):
    model = Users
    json_dumps_kwargs = {u"indent": 2}

    def get(self, request, *args, **kwargs):
        if Users.objects.filter(username__iexact=kwargs['username']):
            context_dict = {u"exists": True}
        else:
            context_dict = {u"exists": False}
        return self.render_json_response(context_dict)
