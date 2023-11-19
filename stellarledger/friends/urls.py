from django.urls import path
from friends import views

urlpatterns = [
    path('addfriend/', views.add_friend, name='addfriend'),
    path('adddebt/<str:name>/', views.add_debt, name='adddebt'),
    path('notify/<str:name>/', views.notify, name='notify'),
    path('viewfriend/', views.view_friends, name='viewFriend'),
]