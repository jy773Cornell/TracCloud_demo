from django import forms
from utils.bootstrap import BootStrapForm


class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="User Name",
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(render_value=True),
        required=True,
    )
    code = forms.CharField(
        label="Please enter the verification code",
        widget=forms.TextInput,
        required=True,
    )
    is_active = forms.BooleanField(
        required=False,
    )

    def clean_is_active(self):
        return True
