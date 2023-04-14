from django.db import models
from user import models as user_model


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


    def __str__(self):
        return f"{self.author}: {self.caption}"


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
