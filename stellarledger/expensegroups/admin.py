from django.contrib import admin
from .models import ExpenseGraph, ExpenseGroup, ExpenseGroupMember, Edge
# Register your models here.

admin.site.register(ExpenseGraph)
admin.site.register(ExpenseGroup)
admin.site.register(ExpenseGroupMember)
admin.site.register(Edge)
