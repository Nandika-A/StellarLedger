from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_username = models.CharField(max_length=20)
    debt = models.DecimalField(decimal_places=2, max_digits=10, blank=True)
    credit = models.DecimalField(decimal_places=2, max_digits=10, blank=True)
    date = models.DateField(blank=True)