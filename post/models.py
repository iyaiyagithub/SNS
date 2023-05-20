import os
from django.conf import settings
from django.db import models
from user import models as user_model
from taggit.managers import TaggableManager


class TimeStamedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)  # 업데이트는 auto_now = True 사용

    class Meta:
        abstract = True


class Post(TimeStamedModel):
    author = models.ForeignKey(
        user_model.User,
        null=True,
        on_delete=models.CASCADE,
        related_name='post_author'
    )
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField(blank=False)
    post_likes = models.ManyToManyField(
        user_model.User, blank=True, related_name='post_like')
    tags = TaggableManager(blank=True)

    @property
    def like_count(self):
        return self.post_likes.count()

    def __str__(self):
        return f"{self.author}: {self.caption}"
    
    def delete(self, *args, **kargs):
        if self.upload_files:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Post, self).delete(*args, **kargs)


class Comment(TimeStamedModel):
    author = models.ForeignKey(
        user_model.User,
        null=True,
        on_delete=models.CASCADE,
        related_name='comment_author'
    )
    posts = models.ForeignKey(
        Post,
        null=True,
        on_delete=models.CASCADE,
        related_name='comment_post'
    )
    contents = models.TextField(blank=False)

    def __str__(self):
        return f"{self.author}: {self.contents}"
