# -*- coding: utf-8 -*-
from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

MIDDLEWARE_CLASSES += (
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    'mocks',
    'lettuce.django',
    'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1',)
