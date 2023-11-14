from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from .models import Transaction
from datetime import date

@shared_task(bind = True)
def recurring_bills(self):
    txn = Transaction.objects.filter(recurring='Yes')
    print("hi")
    users = []
    for t in txn:
        print("1")
        users.append(t.user)
    for u in users:
        print(u)
        t = Transaction.objects.filter(user = u, recurring='Yes', timestamp__gt=date.today())
        html_content = render_to_string('report/reminder.html', {'txn': t,})               
        text_content = "List of your recurring bills"                      
        msg = EmailMultiAlternatives("Recurring bills reminder", text_content, settings.EMAIL_HOST_USER, [u])                                      
        msg.attach_alternative(html_content, "text/html")                                                                                                                                                                               
        msg.send() 
    return "sent" 