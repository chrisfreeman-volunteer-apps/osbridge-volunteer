# -*- coding: utf-8 -*-
# Import the reverse lookup function
# from django.core.urlresolvers import reverse

# view imports
from django.views.generic import DetailView
# from django.views.generic import RedirectView
# from django.views.generic import UpdateView
# from django.views.generic import ListView

# Only authenticated users can access views using this.
from braces.views import JSONResponseMixin  # , #LoginRequiredMixin
from rest_framework import generics

# Import the form from users/forms.py
# from .forms import UserForm

# Import the customized User model
from .models import Users
from .serializers import UserSerializer


# class UserDetailView(LoginRequiredMixin, DetailView):
#     model = Users
#     slug_field = "username"
#     slug_url_kwarg = "username"


# class UserRedirectView(LoginRequiredMixin, RedirectView):
#     permanent = False

#     def get_redirect_url(self):
#         return reverse("users:detail",
#                        kwargs={"username": self.request.user.username})


# class UserUpdateView(LoginRequiredMixin, UpdateView):

#     form_class = UserForm
#     model = Users

#     def get_success_url(self):
#         return reverse("users:detail",
#                        kwargs={"username": self.request.user.username})

#     def get_object(self):
#         # Only get the User record for the user making the request
#         return Users.objects.get(username=self.request.user.username)


# class UserListView(LoginRequiredMixin, ListView):
#     model = Users
#     # These next two lines tell the view to index lookups by username
#     slug_field = "username"
#     slug_url_kwarg = "username"


class UserList(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class UserDetail(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
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
