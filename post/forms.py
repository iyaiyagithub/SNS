from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # model은 Post 양식으로 쓰겠다.
        fields = ('caption', 'image')  # 어떤 필드를 입력 받을 지
        exclude = ('author', )  # 폼에서 author 입력받지 않게 함
