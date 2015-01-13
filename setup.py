#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os # NOQA
import sys # NOQA


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import volunteerapp
version = volunteerapp.__version__

setup(
    name='VolunteerApp',
    version=version,
    author='',
    author_email='hannes.hapke@gmail.com',
    packages=[
        'volunteerapp',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['volunteerapp/manage.py'],
)
