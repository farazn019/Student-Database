
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout


class loginForm(forms.Form):
    UserName = forms.CharField(
        label="Username",
        help_text="Please enter your username",
        widget=forms.TextInput(attrs={"placeholder":"Username"}),
        required=False
    )

    Password = forms.CharField(
        label="Password",
        help_text="Enter your password",
        widget=forms.TextInput(attrs={"placeholder":"Password"}),
        required=False
    )

