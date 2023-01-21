from django import forms
from django.core.validators import ValidationError
from django.contrib.auth.hashers import check_password, make_password
from USER.models import User, UserType
from utils.bootstrap import BootStrapModelForm, BootStrapReadOnlyModelForm


class UserProfileReadOnlyModelForm(BootStrapReadOnlyModelForm):
    class Meta:
        model = User
        exclude = ["uid", "password", "added_by", "self_activated", "is_active", "create_time"]
