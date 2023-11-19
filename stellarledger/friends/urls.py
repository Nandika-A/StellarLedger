from django.urls import path
from friends import views

urlpatterns = [
    path('addfriend/', views.add_friend, name='addfriend'),
    path('adddebt/<int:id>/', views.add_debt, name='adddebt'),
    path('viewfriend/', views.view_friends, name='viewFriend'),
]