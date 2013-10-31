#!/usr/bin/env python
# -*- coding: utf-8 -*-

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

INSTALLED_APPS = (
    'pipeline',
    'raven',
    'newrelic',
)


# Django-Pipeline
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_COMPILERS = (
  'pipeline.compilers.less.LessCompiler',
)

SECRET_KEY = "THIS IS A SEKRIT K3Y LOLZ"
ROOT_URLCONF = "urls"

# Local settings
try:
    import local_settings
except ImportError:
    local_settings = None
