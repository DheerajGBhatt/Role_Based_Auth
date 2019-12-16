from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Roles import views

urlpatterns = [
    path('create/', views.create,name="createrole"), 
    path('view/', views.roles_view,name="roleview"),
    path('action/', views.roles_action,name="assignaction"),
    path('resource/', views.roles_resource,name="assignresource"),  
]
