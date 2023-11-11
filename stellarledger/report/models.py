from django.db import models
from django.contrib.auth import User

# Create your models here.

class Transaction(models.Model):
    sender = models.CharField(max_length=150)
    receiver = models.CharField(max_length=150)
    amount = models.DecimalField()
    timestamp = models.DateTimeField()
    category = models.CharField(max_length=20)

    def __str__(self):
        return (self.sender, self.receiver)

class Category(models.Model):
    category = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.category