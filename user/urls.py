from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('profile_detail/', views.profile_detail, name="profile_detail"),
    path('profile_update/', views.profile_update, name="profile_update"),
]
