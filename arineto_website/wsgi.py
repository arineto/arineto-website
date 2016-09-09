"""
WSGI config for arineto_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arineto_website.settings")

application = get_wsgi_application()

from django.core.wsgi import get_wsgi_application  # noqa
from dj_static import Cling  # noqa

application = Cling(get_wsgi_application())
