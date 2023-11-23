from django.forms import ModelForm
from .models import Friend, Group

class AddFriendForm(ModelForm):
    class Meta:
        model = Friend
        fields = ['friend_username']

class AddGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name']
