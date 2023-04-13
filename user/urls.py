from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('profile-detail/', views.profile_detail, name="profile-detail"),
    path('profile-update/', views.profile_update, name="profile-update"),
]
