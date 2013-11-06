import os
from logging import getLogger

logger = getLogger(__name__)

DJANGO_DEBUG = bool(os.environ.get("DEBUG", False) or
                    os.environ.get("TEST", False))

if not DJANGO_DEBUG or 'DYNO' in os.environ:
    from .conf.prod import *
else:
    from .conf.dev import *
    logger.debug("Imported debug settings")
