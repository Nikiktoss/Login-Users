from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegistrateForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'field__input'}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class': 'field__input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'password__field'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(
        attrs={'class': 'password__field'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
