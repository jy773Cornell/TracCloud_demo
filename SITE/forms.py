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
        queryset=SiteType.objects.filter(level=2, is_active=True),
        to_field_name="name",
        empty_label=None,
        required=True,
    )

    class Meta:
        model = Site
        fields = ["sid", "user", "name", "type", "owner_name", "gps", "gps_system"]

    def clean_sid(self):
        return gen_uuid("SID")
