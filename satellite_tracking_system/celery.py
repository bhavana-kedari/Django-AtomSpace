from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Import the crontab module.
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'satellite_tracking_system.settings')

# Create a Celery instance.
app = Celery('satellite_tracking_system')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks.
app.autodiscover_tasks()

# Define the Celery beat schedule
app.conf.beat_schedule = {
    'update_satellites': {
        'task': 'tracking.tasks.update_satellites_task',
        'schedule': crontab(minute='*/10'),  # Run every 10 minutes
    },
}
app.conf.worker_pool = 'gevent'

