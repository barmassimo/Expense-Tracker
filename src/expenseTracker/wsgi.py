"""
WSGI config for expenseTracker project.
"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "expenseTracker.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


