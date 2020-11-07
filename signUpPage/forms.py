from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout


class RegisterForm(forms.Form):
    Username = forms.CharField(
        label="UserName",
        help_text="Please enter your username: ",
        widget=forms.TextInput(attrs={"Placeholder": "Username"}),
        required=True
    )
    Email = forms.EmailField(
        label="Email",
        help_text="Please enter your email: ",
        widget=forms.TextInput(attrs={"Placeholder": "Email"}),
        required=True
    )
    Password = forms.CharField(
        label="Password",
        help_text="Please enter your password: ",
        widget=forms.TextInput(attrs={"Placeholder": "Password"}),
        required=True
    )