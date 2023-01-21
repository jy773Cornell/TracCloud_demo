from django import forms
from django.core.validators import ValidationError
from django.contrib.auth.hashers import check_password, make_password
from USER.models import User
from utils.bootstrap import BootStrapForm, BootStrapReadOnlyModelForm, BootStrapModelForm


class UserProfileReadOnlyModelForm(BootStrapReadOnlyModelForm):
    class Meta:
        model = User
        exclude = ["uid", "username", "type", "password", "added_by", "self_activated", "is_active", "create_time"]


class PasswordForm(BootStrapForm):
    current_password = forms.CharField(
        label="Current Password",
        widget=forms.PasswordInput(render_value=True),
        required=True,
    )

    new_password = forms.CharField(
        label="New Password",
        min_length=8,
        widget=forms.PasswordInput(render_value=True),
        required=True,
    )

    confirm_password = forms.CharField(
        label="Confirm Password",
        min_length=8,
        widget=forms.PasswordInput(render_value=True),
        required=True,
    )

    def clean_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        return make_password(new_password)

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get("new_password")
        confirm_pwd = self.cleaned_data.get("confirm_password")
        if not check_password(confirm_pwd, new_password):
            raise ValidationError("Passwords do not match.")
        return confirm_pwd
