import os
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_name = models.CharField(blank=True, max_length=255)
    profile_photo = models.ImageField(blank=True, null=True)
    bio = models.TextField(blank=True)
    email = models.CharField(blank=True, max_length=255)

    class Meta:
        db_table = "my_user"

    def get_absolute_url(self):
        return reverse("users:login", kwargs={"username": self.username})

    def delete(self, *args, **kargs):
        if self.upload_files:
            os.remove(os.path.join(
                settings.MEDIA_ROOT, self.profile_photo.path))
        super(User, self).delete(*args, **kargs)
