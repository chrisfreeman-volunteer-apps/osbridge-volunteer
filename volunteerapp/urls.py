# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

from volunteer import views as volunteer_views
from users import views as user_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# set API routers
router = DefaultRouter()
router.register(r'org', volunteer_views.OrganizationViewSet)
router.register(r'events', volunteer_views.EventViewSet)
router.register(r'shifts', volunteer_views.ShiftViewSet)
router.register(r'profile', user_views.UserViewSet)

urlpatterns = patterns('',
    # url(r'^$',  # noqa
    #     TemplateView.as_view(template_name='pages/home.html'),
    #     name="home"),
    # url(r'^about/$',
    #     TemplateView.as_view(template_name='pages/about.html'),
    #     name="about"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^profile/', include("users.urls", namespace="profile")),
    # url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    # url(r'^avatar/', include('avatar.urls')),

    # API urls go here
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
