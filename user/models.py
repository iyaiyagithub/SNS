from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_name = models.CharField(blank=True, max_length=255)
    profile_photo = models.ImageField(blank=True)
    bio = models.TextField(blank=True)
    email = models.CharField(blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:login", kwargs={"username": self.username})