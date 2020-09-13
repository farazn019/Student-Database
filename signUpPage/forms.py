from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(min_length=7, max_length=50)
    password1 = forms.CharField(min_length=8, max_length=80, help_text="<br/> Please enter a unique password that is "
                                                                       "from ""8 to 80 characters long")

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]


