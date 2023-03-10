from django.db import models
from utils.ModelManager import MyModelManager


class User(models.Model):
    uid = models.CharField(verbose_name="UID", primary_key=True, max_length=48)

    username = models.CharField(verbose_name="Username", unique=True, max_length=64)
    password = models.CharField(verbose_name="Password", max_length=128)
    type = models.ForeignKey(verbose_name="User Type", to="UserType", to_field="utid", related_name="user_type",
                             null=True, blank=True, on_delete=models.SET_NULL)

    name = models.CharField(verbose_name="Actual Name", null=True, blank=True, max_length=64)
    business_name = models.CharField(verbose_name="Business Name", null=True, blank=True, max_length=256)
    registration_no = models.CharField(verbose_name="Registration No.", null=True, blank=True, max_length=128)
    reg_expire_date = models.DateField(verbose_name="Registration Expire Date", null=True, blank=True)
    address = models.CharField(verbose_name="Address", null=True, blank=True, max_length=256)
    city = models.CharField(verbose_name="City", null=True, blank=True, max_length=64)
    county = models.CharField(verbose_name="County", null=True, blank=True, max_length=64)
    state = models.CharField(verbose_name="State", null=True, blank=True, max_length=64)
    zipcode = models.CharField(verbose_name="Zip Code", null=True, blank=True, max_length=16)
    country = models.CharField(verbose_name="Country", null=True, blank=True, max_length=64)
    phone = models.CharField(verbose_name="Phone Number", null=True, blank=True, max_length=16)
    cell = models.CharField(verbose_name="Cell Number", null=True, blank=True, max_length=16)
    email = models.EmailField(verbose_name="Email", null=True, blank=True)

    added_by = models.ForeignKey(verbose_name="Added By", to="User", to_field="uid", related_name="user_added_by",
                                 null=True, blank=True, on_delete=models.SET_NULL)
    self_activated = models.BooleanField(verbose_name="Self Activated", default=False)
    is_active = models.BooleanField(verbose_name="Is Active", default=False)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("UID")

    def __str__(self):
        return "{} ({})".format(self.username, self.type)


class UserType(models.Model):
    utid = models.CharField(verbose_name="UTID", primary_key=True, max_length=48)
    name = models.CharField(verbose_name="Type Name", unique=True, max_length=128)
    info_data_table = models.CharField(verbose_name="Info Data Table", null=True, blank=True, max_length=256)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("UTID")

    def __str__(self):
        return self.name


class UserRelation(models.Model):
    urid = models.CharField(verbose_name="URID", primary_key=True, max_length=48)
    requester = models.ForeignKey(verbose_name="Requester", to="User", to_field="uid", related_name="requester_user",
                                  null=True, blank=True, on_delete=models.SET_NULL)
    provider = models.ForeignKey(verbose_name="Provider", to="User", to_field="uid", related_name="provider_user",
                                 null=True, blank=True, on_delete=models.SET_NULL)
    relation_type = models.ForeignKey(verbose_name="Relation Type", to="UserRelationType", to_field="urtid",
                                      related_name="relationtype", null=True, blank=True, on_delete=models.SET_NULL)
    added_by = models.ForeignKey(verbose_name="Added By", to="User", to_field="uid", related_name="relation_added_by",
                                 null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(verbose_name="Is Active", default=False)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("URID")

    def __str__(self):
        return "Relation: {}, Requester: {}, Provider: {}".format(self.relation_type, self.requester, self.provider)


class UserRelationType(models.Model):
    urtid = models.CharField(verbose_name="URTID", primary_key=True, max_length=48)
    name = models.CharField(verbose_name="Type Name", unique=True, max_length=128)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("URTID")

    def __str__(self):
        return self.name
