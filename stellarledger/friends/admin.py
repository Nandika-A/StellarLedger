from django.contrib import admin
from .models import Friend, Group, UserGroup, PairExpenses, Expense_group_members, Expense_group
# Register your models here.
admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(UserGroup)
admin.site.register(PairExpenses)
admin.site.register(Expense_group)
admin.site.register(Expense_group_members)