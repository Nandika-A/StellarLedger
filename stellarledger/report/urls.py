from django.urls import path
from report import views

urlpatterns = [
    path('record/', views.recordTransaction, name='record'),
    path('addcategory/', views.createCategory, name='create'),
    path('viewTransactions/', views.viewTransactions, name='viewTransaction'),
    path('viewCategories/', views.viewCategory, name='viewCategories'),
    path('deleteCategory/<int:id>/', views.deleteCategory, name='deleteCategory'),
    path('updatecategory/<int:id>/', views.changeTransactionCategory, name='changecategory'),
    path('deleteTransaction/<int:id>/', views.deleteTransaction, name='deleteTransaction'),
    path('recurringbills/', views.recurringbills, name='recurring')
]