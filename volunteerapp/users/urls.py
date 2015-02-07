# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns(
    '',
    url(
        regex=r'^exists/(?P<username>[\w.@+-]+)/$',
        view=views.UsernameAJAXView.as_view(),
        name='username-check'
    ),
)
