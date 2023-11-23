from django.db import models
from django.contrib.auth.models import User

class ExpenseGroup(models.Model):
    name = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)

class ExpenseGroupMember(models.Model):
    group = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ExpenseGraph(models.Model):
    group = models.OneToOneField(ExpenseGroup, on_delete=models.CASCADE)

class Edge(models.Model):
    graph = models.ForeignKey(ExpenseGraph, on_delete=models.CASCADE)
    debtor = models.ForeignKey(ExpenseGroupMember, related_name='debtor', on_delete=models.CASCADE)
    creditor = models.ForeignKey(ExpenseGroupMember, related_name='creditor', on_delete=models.CASCADE)
    amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, blank=True)
    title = models.CharField(max_length=10)