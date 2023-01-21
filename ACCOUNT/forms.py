from django import forms
from django.core.validators import ValidationError
from django.contrib.auth.hashers import check_password, make_password
from USER.models import User, UserType
from utils.UUIDGen import gen_uuid
from utils.bootstrap import BootStrapForm, BootStrapModelForm


class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="Username",
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


class UserCreateForm(BootStrapModelForm):
    uid = forms.CharField(required=False)

    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(render_value=True),
    )

    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(render_value=True),
    )

    email = forms.CharField(required=True)

    type = forms.ModelChoiceField(
        queryset=UserType.objects.exclude(type_name="admin").filter(is_active=True),
        to_field_name="type_name",
        empty_label=None,
        required=True,
    )

    class Meta:
        model = User
        fields = ["uid", "username", "type", "password", "email"]

    def clean_uid(self):
        return gen_uuid("UID")

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return make_password(password)

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_pwd = self.cleaned_data.get("confirm_password")
        if not check_password(confirm_pwd, password):
            raise ValidationError("Passwords do not match.")
        return confirm_pwd
