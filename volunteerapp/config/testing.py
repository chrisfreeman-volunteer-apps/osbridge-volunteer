# -*- coding: utf-8 -*-
'''
Testing Configurations

- Runs in Production mode
- Uses console backend for emails
'''
from configurations import values
from .common import Common


class Testing(Common):

    # DEBUG
    DEBUG = values.BooleanValue(False)
    TEMPLATE_DEBUG = DEBUG
    # END DEBUG

    # INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    # END INSTALLED_APPS

    # Mail settings
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')
    # End mail settings

    # INSTALLED_APPS += ('')

    INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)
    ALLOWED_HOSTS = ["*"]

    # DATABASES CONFIGURATION

    DATABASES = values.DatabaseURLValue('postgres://postgres' +
                                        '@127.0.0.1:5432/' +
                                        'volunteerapp')
    # END DATABASE CONFIGURATION

    # Your local stuff: Below this line define 3rd party library settings
