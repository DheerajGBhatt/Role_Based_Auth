from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Users import views



urlpatterns = [
    path("login/", views.login_request, name="login"),
    path("home/", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path('create/', views.create, name="createuser"), 
    path('view/', views.user_view, name="userview"),
    path('roles/', views.user_role, name="assignrole"),
]
