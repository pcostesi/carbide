from __future__ import with_statement

import os

from fabric.api import *
from fabric.contrib.console import confirm
from fabric.operations import prompt

base_path = os.path.abspath(os.path.dirname(__file__))


def test():
    with prefix(". env/bin/activate"):
        local("python manage.py harvest")
        local("python manage.py test")


# def django_translate(user="www-data"):
#     with prefix(". env/bin/activate"):
#         sudo("python manage.py compilemessages", user=user)
#         sudo("python manage.py collectstatic --noinput", user=user)
#         sudo("python manage.py clean_pyc")
#         sudo("python manage.py compile_pyc", user=user)


# def django_deploy(branch=None, user="www-data"):
#     with prefix(". env/bin/activate"):
#         sudo("pip install -r dependencies.txt", user=user)
#         sudo("python manage.py syncdb", user=user)
#         sudo("python manage.py migrate", user=user)
#     django_translate(user)


def install_dependencies():
    local("sudo apt-get install libpq-dev libxml2-dev libxslt-dev")
    local("sudo pip install virtualenv")


def create_venv():
    local("virtualenv env")


def install_git_hooks():
    try:
        os.unlink(os.path.join(base_path, ".git/hooks/pre-commit"))
    except OSError:
        pass
    local("ln -s %s/hooks/pre-commit %s/.git/hooks/pre-commit" % (
        base_path, base_path))


def run(port=8080):
    with prefix(". env/bin/activate"):
        # local("python manage.py runserver 0.0.0.0:%s" % (port,))
        local("python manage.py collectstatic --noinput --link")
        local("foreman start")


def clean():
    with prefix(". env/bin/activate"):
        local("python manage.py clean_pyc")


def pip_install():
    with prefix(". env/bin/activate"):
        local("pip install -r requirements.txt")


def setup_heroku():
    local("heroku config:add BUILDPACK_"
          "URL=https://github.com/sabf/heroku-buildpack-multi.git")


def npm_install():
    local("npm install")


def heroku_toolbelt():
    local("wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh")


def setup_env_vars():
    key = prompt("What is your key?")
    debug = confirm("Setup debug?")
    with open(".env", "wb") as f:
        f.write("DJANGO_SECRET_KEY=%s\n" % (key,))
        if debug:
            f.write("DEBUG=%s\n" % (debug,))


def install():
    install_dependencies()
    heroku_toolbelt()
    install_git_hooks()
    create_venv()
    pip_install()
    npm_install()
    setup_env_vars()
