from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('my-posts/', views.my_posts, name="my-posts"),
    path('<int:user_id>/my-posts/', views.edit_profile, name="edit-profile"),
]
