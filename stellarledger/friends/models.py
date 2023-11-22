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
    due_date = models.DateField(null=True, blank=True)

class Group(models.Model):
    name = models.CharField(max_length=10)
    debt = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, blank=True)
    debt_paid_to = models.CharField(null=True, blank=True, max_length=20)

class UserGroup(models.Model):
    Ch = [
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    paid = models.CharField(max_length=3, choices=Ch, default='NO')

class Expense_group(models.Model):
    name = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)

class Expense_group_members(models.Model):
    group = models.ForeignKey(Expense_group, on_delete=models.CASCADE)
    member1 = models.ForeignKey(User, on_delete=models.CASCADE)

class PairExpenses(models.Model):
    member1 = models.ForeignKey(Expense_group_members, on_delete=models.CASCADE)
    member2 = models.CharField(max_length=10)
    pay1to2 = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, blank=True)
    title = models.CharField(max_length=10)