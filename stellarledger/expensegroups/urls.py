from django.urls import path
from expensegroups import views

urlpatterns = [
    path('view_expense_groups/', views.view_expense_groups, name='view_expense_groups'),
    path('add_expense_group/', views.add_expense_group, name='add_expense_group'),
    path('add_members/<int:id>/', views.add_members, name='add_members'),
    path('add_txn/<int:id>/', views.add_txn, name='add_txn'),
    path('view_all_transactions/<int:id>/', views.view_all_transactions, name='view_all_transactions'),
    path('view_simplified_txns/<int:id>/', views.view_simplified_txns, name='view_simplified_txns'),
]