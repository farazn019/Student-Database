
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout


class loginForm(forms.Form):
    UserName = forms.CharField(
        label="Username",
        help_text="Please enter your username",
        widget=forms.TextInput(attrs={"placeholder":"Username"}),
        required=True
    )

    Password = forms.CharField(
        label="Password",
        help_text="Enter your password",
        widget=forms.TextInput(attrs={"placeholder":"Password"}),
        required=True
    )
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_id = "id-loginform"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_survey"

        self.helper.layout = Layout(
            Fieldset(
                "Login Form",
                "Username",
                "Password"
            )
        )'''
