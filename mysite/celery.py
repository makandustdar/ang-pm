from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Default Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')

# Using a string here eliminates the need to serialize
# the configuration object to child processes by the Celery worker.

# - namespace='CELERY' means all celery-related configuration keys
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django applications.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

from datetime import timedelta

app.conf.beat_schedule = {
    # Scheduler Name
    'check-review-due': {
        # Task Name (Name Specified in Decorator)
        'task': 'check_review_due',
        # Schedule
        'schedule': crontab(minute=0, hour=10),
    },
}
