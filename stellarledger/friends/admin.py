from django.contrib import admin
from .models import Friend, Group, UserGroup
# Register your models here.
admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(UserGroup)