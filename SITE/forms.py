import requests
from django import forms
from django.core.validators import ValidationError
from django.contrib.auth.hashers import check_password, make_password
from USER.models import User, UserType
from SITE.models import Site, SiteType
from utils.UUIDGen import gen_uuid
from utils.bootstrap import BootStrapForm, BootStrapModelForm, BootStrapReadOnlyModelForm


class TopSiteModelForm(BootStrapModelForm):
    sid = forms.CharField(required=False)

    user = forms.CharField(required=False)

    type = forms.ModelChoiceField(
        queryset=SiteType.objects.filter(level=1, is_active=True),
        to_field_name="name",
        required=True,
    )

    class Meta:
        model = Site
        fields = ["sid", "user", "type", "name", "owner_name", "gps", "gps_system"]

    def clean_sid(self):
        return gen_uuid("SID")


class MiddleSiteModelForm(BootStrapModelForm):
    sid = forms.CharField(required=False)

    user = forms.CharField(required=False)

    parent_type = forms.CharField(required=False)

    type = forms.ModelChoiceField(
        queryset=SiteType.objects.filter(level=2, is_active=True),
        to_field_name="name",
        required=True,
    )

    class Meta:
        model = Site
        fields = ["sid", "user", "type", "name", "parent_type"]

    def clean_sid(self):
        return gen_uuid("SID")


class BaseSiteModelForm(BootStrapModelForm):
    sid = forms.CharField(required=False)

    user = forms.CharField(required=False)

    size = forms.FloatField(required=True)

    type = forms.ModelChoiceField(
        queryset=SiteType.objects.filter(level=3, is_active=True),
        to_field_name="name",
        empty_label=None,
        required=True,
    )

    class Meta:
        model = Site
        fields = ["sid", "user", "crop", "crop_year", "type", "name", "size", "size_unit"]

    def clean_sid(self):
        return gen_uuid("SID")
