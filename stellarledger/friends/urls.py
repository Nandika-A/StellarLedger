from django.urls import path
from friends import views

urlpatterns = [
    path('addfriend/', views.add_friend, name='addfriend'),
    path('adddebt/<str:name>/', views.add_debt, name='adddebt'),
    path('notify/<str:name>/', views.notify, name='notify'),
    path('viewfriend/', views.view_friends, name='viewFriend'),
    path('viewgroup/', views.view_groups, name='viewGroup'),
    path('addgroup/', views.add_group, name='addgroup'),
    path('addtogroup/<int:id>/', views.addtogroup, name='addtogroup'),
    path('viewgroupmem/<int:id>/', views.viewgroupmem, name='viewGroupmem'),
    path('resolve/<int:id>/', views.resolvegroupdebt, name='resolve'),
    path('updatedebt/<int:id>/', views.updatedebt, name='updatedebt'),
    path('approve/<int:pk>/', views.approve, name='approve'),
]