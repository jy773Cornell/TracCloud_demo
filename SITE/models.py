from django.db import models
from utils.ModelManager import MyModelManager


class Site(models.Model):
    sid = models.CharField(verbose_name="SID", primary_key=True, max_length=48)
    user = models.ForeignKey(verbose_name="User", to="USER.User", to_field="uid", related_name="site_user",
                             null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(verbose_name="Site Name", max_length=256)
    owner_name = models.CharField(verbose_name="Owner Name", max_length=64)
    type = models.ForeignKey(verbose_name="Type", to="SiteType", to_field="stid", related_name="site_type",
                             null=True, blank=True, on_delete=models.SET_NULL)
    crop = models.ForeignKey(verbose_name="Crop", to="CROP.Crop", to_field="cid", related_name="site_crop",
                             null=True, blank=True, on_delete=models.SET_NULL)
    variety = models.ForeignKey(verbose_name="Variety", to="SiteVariety", to_field="svid",
                                related_name="site_variety", null=True, blank=True, on_delete=models.SET_NULL)
    crop_year = models.IntegerField(verbose_name="Crop Year", null=True, blank=True)
    size = models.FloatField(verbose_name="Size", null=True, blank=True)
    size_unit = models.ForeignKey(verbose_name="Size Unit", to="SiteUnit", to_field="suid", related_name="site_unit",
                                  null=True, blank=True, on_delete=models.SET_NULL)
    gps = models.CharField(verbose_name="GPS", null=True, blank=True, max_length=128)
    gps_system = models.CharField(verbose_name="GPS System", null=True, blank=True, max_length=64)
    parent = models.ForeignKey(verbose_name="Parent Site", to="Site", to_field="sid", related_name="site_site",
                               null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("SID")

    def __str__(self):
        return self.name


class SiteType(models.Model):
    stid = models.CharField(verbose_name="STID", primary_key=True, max_length=48)
    name = models.CharField(verbose_name="Type Name", max_length=128)

    level_choices = (
        (1, "parent"),
        (2, "child"),
    )
    level = models.SmallIntegerField(verbose_name="Level", choices=level_choices)

    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("CGSID")

    def __str__(self):
        return self.name


class SiteUnit(models.Model):
    suid = models.CharField(verbose_name="SUID", primary_key=True, max_length=48)
    unit = models.CharField(verbose_name="Unit", max_length=32)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("SUID")

    def __str__(self):
        return self.unit


class SiteVariety(models.Model):
    svid = models.CharField(verbose_name="SVID", primary_key=True, max_length=48)
    name = models.CharField(verbose_name="Variety Name", max_length=32)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("SVID")

    def __str__(self):
        return self.name
