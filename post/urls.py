from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('post-view/', views.post_view, name='post-view'),
    path('write-post/', views.write_post, name='write-post'),
    path('post-detail/', views.post_detail, name='post-detail'),
    path('delete-post/', views.delete_post, name='delete-post'),
    path('edit-post/', views.edit_post, name='edit-post'),

]