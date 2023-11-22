from django.forms import ModelForm
from .models import Friend, Group, Expense_group

class AddFriendForm(ModelForm):
    class Meta:
        model = Friend
        fields = ['friend_username']

class AddGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name']

class AddExpenseGroupForm(ModelForm):
    class Meta:
        model = Expense_group
        fields = ['name', 'description']