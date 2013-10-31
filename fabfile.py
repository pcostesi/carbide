from __future__ import with_statement

import os
from contextlib import contextmanager

from fabric.api import *
from fabric.contrib.console import confirm
from fabric.contrib.files import upload_template


def test():
    with prefix(". env/bin/activate"):
        local("python app/manage.py harvest features")
        local("python app/manage.py test")

def django_translate(user="www-data"):
    with prefix("source env/bin/activate"):
        sudo("cd app && python manage.py compilemessages", user=user)
        sudo("cd app && python manage.py collectstatic --noinput", user=user)
        sudo("cd app && python manage.py clean_pyc")
        sudo("cd app && python manage.py compile_pyc", user=user)

def django_deploy(branch=None, user="www-data"):
    with prefix("source bin/activate"):
        sudo("pip install -r dependencies.txt", user=user)
        sudo("python app/manage.py syncdb", user=user)
        sudo("python app/manage.py migrate", user=user)
    django_translate(user)

def install_git_hooks():
    local("cp hooks/* .git/hooks/")