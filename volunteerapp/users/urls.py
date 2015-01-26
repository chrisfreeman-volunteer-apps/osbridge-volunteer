# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    # URL pattern for the UserListView  # noqa
    # url(
    #     regex=r'^$',
    #     view=views.UserListView.as_view(),
    #     name='list'
    # ),
    # # URL pattern for the UserRedirectView
    # url(
    #     regex=r'^~redirect/$',
    #     view=views.UserRedirectView.as_view(),
    #     name='redirect'
    # ),
    # # URL pattern for the UserDetailView
    # url(
    #     regex=r'^(?P<username>[\w.@+-]+)/$',
    #     view=views.UserDetailView.as_view(),
    #     name='detail'
    # ),
    # # URL pattern for the UserUpdateView
    # url(
    #     regex=r'^~update/$',
    #     view=views.UserUpdateView.as_view(),
    #     name='update'
    # ),
    url(r'^$', views.UserList.as_view()),
    url(r'^(?P<username>[\w.@+-]+)/$', views.UserDetail.as_view()),
    url(
        regex=r'^exists/(?P<username>[\w.@+-]+)/$',
        view=views.UsernameAJAXView.as_view(),
        name='username-check'
    ),
)
