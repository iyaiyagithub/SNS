from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    # path('profile/', views.profile, name="profile"),
]