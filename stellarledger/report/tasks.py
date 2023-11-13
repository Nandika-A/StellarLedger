from celery import shared_task
from django.core.mail import send_mail
from .models import Transaction
from django_celery_beat.models import PeriodicTask, CrontabSchedule

@shared_task(bind = True)
def recurring_bills(self):
    txn = Transaction.objects.filter(recurring='Yes')
    users = []
    for t in txn:
        users.append(t.user)
    schedule, created = CrontabSchedule.objects.get_or_create(day_of_week = 'sunday')
    task = PeriodicTask.objects.create(crontab=schedule)