from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control ps-5',
            'placeholder': 'Имя пользователя',
            'name': 'username',
            'minlength': '4',
            'maxlength': '10'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control ps-5',
            'placeholder': 'Пароль',
            'name': 'password1',
            'minlength': '8',
            'maxlength': '20'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control ps-5',
            'placeholder': 'Пароль ещё раз',
            'name': 'password2',
            'minlength': '8',
            'maxlength': '20'
        })
        

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
