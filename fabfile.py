from __future__ import with_statement

import os
from contextlib import contextmanager

from fabric.api import *
from fabric.contrib.console import confirm
from fabric.contrib.files import upload_template


def test():
    with prefix(". env/bin/activate"):
        local("python manage.py harvest")
        local("python manage.py test")

def django_translate(user="www-data"):
    with prefix(". env/bin/activate"):
        sudo("python manage.py compilemessages", user=user)
        sudo("python manage.py collectstatic --noinput", user=user)
        sudo("python manage.py clean_pyc")
        sudo("python manage.py compile_pyc", user=user)

def django_deploy(branch=None, user="www-data"):
    with prefix(". env/bin/activate"):
        sudo("pip install -r dependencies.txt", user=user)
        sudo("python manage.py syncdb", user=user)
        sudo("python manage.py migrate", user=user)
    django_translate(user)

def install_dependencies():
    local("sudo apt-get install libpq-dev libxml2-dev libxslt-dev")
    local("pip install --user virtualenv")

def create_venv():
    local("virtualenv env")

def install_git_hooks():
    local("rm $(pwd)/.git/hooks/pre-commit")
    local("ln -s $(pwd)/hooks/pre-commit $(pwd)/.git/hooks/pre-commit")

def run(port=8080):
    with prefix(". env/bin/activate"):
        local("python manage.py runserver %s" % (port,))

def clean():
    with prefix(". env/bin/activate"):
        local("python manage.py clean_pyc")
