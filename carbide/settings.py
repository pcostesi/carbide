import os

DJANGO_DEBUG = bool(os.environ.get("DEBUG", False))

if not DJANGO_DEBUG or 'DYNO' in os.environ:
    from .conf.prod import *
else:
    from .conf.dev import *
    print "Imported dev"
    print INSTALLED_APPS
