from django.db import models
from django.contrib.auth import User

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
    amount = models.DecimalField()
    timestamp = models.DateTimeField()
    category = models.CharField(max_length=20)
    recurring = models.CharField(max_length=3, choices=PAID, default='Yes')

    def __str__(self):
        return self.to_or_from

class Category(models.Model):
    category = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.category