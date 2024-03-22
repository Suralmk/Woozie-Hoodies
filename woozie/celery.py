import os 
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'woozie.settings')

celery_app = Celery('woozie')

# Configure Celery using settings from Django settings module
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()
