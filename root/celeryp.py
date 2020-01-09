import os
from celery import Celery
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

app = Celery(config('CELERY_NAME_APP'))

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
