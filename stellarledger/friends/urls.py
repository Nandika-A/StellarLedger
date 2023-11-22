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
    path('approve/<int:g_id>/<int:m_id>/', views.approve, name='approve'),
    path('create_expense_group', views.create_expense_group, name='create_expense_group'),
    path('add_expensegrp_members/<int:id>/', views.add_expensegrp_members, name='add_expensegrp_members'),
    path('group_txn/<int:id>', views.group_txn, name='group_txn'),
    path('simplify_debt/<int:id>', views.simplify_debt, name='simplify_debt'),
    path('view_group_debts/<int:id>', views.view_group_debts, name='view_group_debts'),
    path('view_expense_groups', views.view_expense_groups, name='view_expense_groups'),
]