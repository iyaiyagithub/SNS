from django.contrib import admin
from .models import Post
from django.utils.translation import gettext_lazy as _

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'caption', 'create_at', 'updated_at', 'image']
    list_display_links = ['id', 'author', 'caption']




