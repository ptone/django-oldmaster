"""
WSGI config for {{ project_name }} project.

This module contains the actual WSGI application to be used by Django's
development server and the production environment as the global variable
named ``application`` and is enabled by setting the ``WSGI_APPLICATION``
setting to '{{ project_name }}.wsgi.application'.

Of course usually you would have an actual Django WSGI application here,
but it also might make sense to replace the whole Django WSGI application
with a custom one that later delegates to the Django one (for instance if
you want to combine a Django application with an application of another
framework).
"""
from django.core.management import setup_settings

settings = setup_settings(__name__)

# The application object is used by the development server
# as well as a WSGI server configured to use this file.
from django.core.handlers.wsgi import application

# Apply other WSGI middlewares here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
