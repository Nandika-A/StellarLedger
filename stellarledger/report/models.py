from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Transaction(models.Model):
    PAID = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

    ROLE=[
        ('sender','sender'),
        ('receiver', 'receiver')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=10, choices=ROLE, default="sender")
    to_or_from = models.CharField(max_length=150)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    timestamp = models.DateField()
    category = models.CharField(max_length=20)
    recurring = models.CharField(blank = True, max_length=3, choices=PAID, default='Yes')
    r_freq = models.IntegerField(default=0, blank=True)
    r_period =models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.to_or_from

class Category(models.Model):
    category = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.category