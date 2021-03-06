"""
WSGI config for mapit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from mapit.bookit.startup import Startup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mapit.settings")

startup = Startup()
startup.run()

application = get_wsgi_application()
