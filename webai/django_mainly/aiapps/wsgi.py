import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.append('/home/bitnami/apps/django/aiapps')
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/bitnami/apps/django/aiapps/egg_cache")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aiapps.settings')
application = get_wsgi_application()