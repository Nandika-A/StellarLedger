from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stellarledger.settings')

app = Celery('stellarledger')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send-mail-for-recurring-bills': {
        'task': 'report.tasks.recurring_bills',
        # 'schedule': crontab(day_of_week='sunday', minute=0, hour=9)
        'schedule':crontab(hour=13, minute=12)
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')