from django import forms
# from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, User
from . models import RegisterUser


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')
        self.fields.pop('password1')
    widgets = {
        forms.EmailInput(attrs={'class': 'form-control'}),
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}),
                        min_length=8, max_length=60),
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                        min_length=8, max_length=80),
    }
