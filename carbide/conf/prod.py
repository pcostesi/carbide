# -*- coding: utf-8 -*-
import dj_database_url
from .base import *
from . import get_env_setting

SECRET_KEY = get_env_setting("DJANGO_SECRET_KEY")

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ("Pablo Alejandro Costesich", "pablo.costesich@sabf.org.ar"),
)

DEBUG = False
TEMPLATE_DEBUG = False

# MIDDLEWARE_CLASSES += (
#     ,
# )

DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
