from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='customer-home'),
    path('register/', views.register, name='customer-register'),
    path('login/', views.login, name='customer-login'),
    path('login/register', views.register, name='customer-register'),
    path('register/login/', views.home, name='customer-home')
]