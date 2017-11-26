import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ITmap.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)