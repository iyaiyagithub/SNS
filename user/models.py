from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    nickname = models.CharField(blank=True, max_length=255)
    profile_image = models.ImageField(blank=True)
    profile_comment = models.TextField(blank=True)
    email = models.CharField(blank=True, max_length=255)

# 본인 프로필 수정 / 
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # User모델과 Profile을 1:1로 연결
#     description = models.TextField(blank=True)
#     nickname = models.CharField(max_length=40, blank=True)
#     image = models.ImageField(blank=True)