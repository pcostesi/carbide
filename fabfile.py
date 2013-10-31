from __future__ import with_statement

import os
from contextlib import contextmanager

from fabric.api import *
from fabric.contrib.console import confirm
from fabric.contrib.files import upload_template


def test():
    with prefix("source env/bin/activate"):
        local("python manage.py harvest features")
        local("python manage.py test")

def django_translate(user="www-data"):
    with prefix("source env/bin/activate"):
        sudo("python manage.py compilemessages", user=user)
        sudo("python manage.py collectstatic --noinput", user=user)
        sudo("python manage.py clean_pyc")
        sudo("python manage.py compile_pyc", user=user)

def django_deploy(branch=None, user="www-data"):
    with prefix("source bin/activate"):
        sudo("pip install -r dependencies.txt", user=user)
        sudo("python manage.py syncdb", user=user)
        sudo("python manage.py migrate", user=user)
    django_translate(user)

def install_git_hooks():
    local("ln -s hooks/pre-commit .git/hooks/pre-commit")

def venv():
    local("source env/bin/activate")
