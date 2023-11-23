from django.forms import ModelForm
from .models import ExpenseGroupMember, ExpenseGroup

class AddExpenseGroupForm(ModelForm):
    class Meta:
        model = ExpenseGroup
        fields = ['name', 'description']

class AddExpenseGroupMemberForm(ModelForm):
    class Meta:
        model = ExpenseGroupMember
        fields = ['user']