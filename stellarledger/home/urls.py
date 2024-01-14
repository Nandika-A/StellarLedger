from django.urls import path
from home import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('eth/', views.trackethereum, name='eth')
]