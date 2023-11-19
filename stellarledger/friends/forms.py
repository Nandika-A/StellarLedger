from django.forms import ModelForm
from .models import Friend

class AddFriendForm(ModelForm):
    class Meta:
        model = Friend
        fields = ['friend_username']