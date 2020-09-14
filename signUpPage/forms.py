from django import forms
# from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth.models import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, ButtonHolder, Submit
from . models import RegisterUser


class RegisterForm(forms.Form):
    Username = forms.CharField(
        label="UserName",
        required=True
    )
    Email = forms.EmailField(
        label="Email",
        required=True
    )
    Password = forms.CharField(
        label="Password",
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Made IT!")
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.layout = Layout(
            Fieldset(
                'Registration Information',
                'Username',
                'Email',
                'Password'
            ),
        )
