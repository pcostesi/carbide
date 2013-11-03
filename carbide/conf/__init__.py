import os
import site


# taken from https://github.com/nigma/django-modern-template
def rel(*path):
    """
    Converts path relative to the project root into an absolute path

    :rtype: str
    """
    return os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            os.path.pardir, os.path.pardir,
            *path
        )
    ).replace("\\", "/")

site.addpackage(rel("carbide"), "apps.pth", known_paths=set())


def get_env_setting(setting):
    """
    Get the environment setting or raise exception

    :rtype: str
    """
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured(error_msg)
