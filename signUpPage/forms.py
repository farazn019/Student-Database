from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout


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
        self.helper = FormHelper()
        self.helper.form_id = 'id-signUpForm'
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
