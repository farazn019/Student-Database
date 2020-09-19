
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout


class loginForm(forms.Form):
    UserName = forms.CharField(
        label="Username",
        required=True
    )

    Password = forms.CharField(
        label="Password",
        required=True
    )

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_id = "id-loginform"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_survey"

        self.helper.Layout(
            "Login Form",
            "Username",
            "Password"
        )
