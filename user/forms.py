from django.contrib.auth import get_user_model
from django import forms as django_form

User = get_user_model()


class SignUpForm(django_form.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'username', 'password']

        widgets = {
            'password': django_form.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user