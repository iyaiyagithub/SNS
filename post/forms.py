from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    caption = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'caption-contents'}))

    class Meta:
        model = Post  # model은 Post 양식으로 쓰겠다.
        fields = ('caption', 'image')  # 어떤 필드를 입력 받을 지

        labels = {
            "caption": "내용",
            "image": "사진"
        }

class CommentForm(forms.ModelForm):
    contents = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input-comment2', 'placeholder':'댓글 달기..'}))

    class Meta:
        model = Comment
        fields = ["contents"]