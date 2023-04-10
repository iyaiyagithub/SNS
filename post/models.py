from django.db import models
from user import models as user_model

# Create your models here.

class TimeStamedModel(models.Model):
    update_at = models.DateTimeField(auto_now_add=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True # 상속이 되는 베이스 모델
    
class Post(TimeStamedModel):
    author = models.ForeignKey(user_model.User, null=True, on_delete=models.CASCADE, relasted_name='post_author')
    image = models.ImageField(blank=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    content = models.TextField(blank=True)
    








#   author
#     image = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
#     content = models.CharField