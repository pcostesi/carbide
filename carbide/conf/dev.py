# -*- coding: utf-8 -*-
from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = "THIS IS A FAKE KEY"

MIDDLEWARE_CLASSES += (
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

STATICFILES_FINDERS += (
    'pipeline.finders.PipelineFinder',
    'pipeline.finders.CachedFileFinder',
)

INSTALLED_APPS += (
    #'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    'debug_toolbar.panels.profiling.ProfilingDebugPanel',
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db',
        # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        # Empty for localhost through domain sockets or '127.0.0.1' for
        # localhost through TCP.
        'PORT': '',
        # Set to empty string for default.
    }
}
