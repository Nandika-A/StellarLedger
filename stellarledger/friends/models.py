from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_username = models.CharField(max_length=20)
    debt = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, blank=True)
    credit = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, blank=True)
    date = models.DateField(default=date.today(), blank=True)
    due_date = models.DateField(default=date.today(), blank=True)