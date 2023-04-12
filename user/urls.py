from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    
    path('profile/<int:id>', views.profile, name='profile'),
]