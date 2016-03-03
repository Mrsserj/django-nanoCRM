import os, sys

path = '/home/serj/data/CRM'
if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "CRM.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
