from django.contrib.auth import get_user_model
from django import forms as django_forms


User = get_user_model()


class SignUpForm(django_forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'username', 'password']

        widgets = {
            'email': django_forms.TextInput(attrs={'class': 'get-input', 'placeholder': '이메일 주소'}),
            'name': django_forms.TextInput(attrs={'class': 'get-input', 'placeholder': '성명'}),
            'username': django_forms.TextInput(attrs={'class': 'get-input', 'placeholder': '사용자 이름'}),
            'password': django_forms.PasswordInput(attrs={'class': 'get-input', 'placeholder': '비밀번호'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserUpdateForm(django_forms.ModelForm):
    name = django_forms.CharField()
