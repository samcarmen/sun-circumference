import os
from celery import Celery
from django.conf import settings
from pi_calculator.utils import compute_pi_indefinitely

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sun_circumference.settings")

app = Celery("sun_circumference")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
