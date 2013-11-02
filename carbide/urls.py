# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from mocks.views import LoginView

urlpatterns = patterns('',
    url(r"", include('mocks.urls')),
    )
