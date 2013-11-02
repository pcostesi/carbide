from django.conf.urls.defaults import patterns, include, url

from mocks.views import LoginView

urlpatterns = patterns("",
    url(r'^login/?$', LoginView.as_view(), name='login'),
    )
