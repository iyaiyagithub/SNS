from django.contrib import admin
from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.user_feed, name='feed'),
    path('write-post/', views.write_post, name='write-post'),
    path('post-detail/<int:id>', views.post_detail, name='post-detail'),
    path('delete-post/<int:id>', views.delete_post, name='delete-post'),
    path('edit-post/<int:id>', views.edit_post, name='edit-post'),

    path('search/', views.search, name='post_search'),

    path('<int:post_id>/comment_create',
         views.comment_create, name='comment_create'),
    path('<int:comment_id>/comment_delete',
         views.comment_delete, name='comment_delete'),

    path('post_like/<int:post_id>', views.post_like, name='post_like'),

    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(),
         name='tagged_object_list'),
]
