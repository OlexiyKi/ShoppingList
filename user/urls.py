from django.urls import path, include
from . import views

urlpatterns = [
    path('/login', views.user_login, name='user_login'),
    path('/register', views.user_register, name='register'),
    path('/logout', views.user_logout, name='logout'),

 ]