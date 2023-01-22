from django.db import models
from utils.ModelManager import MyModelManager


class Equipment(models.Model):
    eid = models.CharField(verbose_name="EID", primary_key=True, max_length=48)
    user = models.ForeignKey(verbose_name="User", to="USER.User", to_field="uid", related_name="equip_user",
                             null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(verbose_name="Equipment Name", max_length=64)
    type = models.ForeignKey(verbose_name="Type", to="EquipmentType", to_field="etid",
                             related_name="equip_type", null=True, blank=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(verbose_name="Owner", to="USER.User", to_field="uid", related_name="owner_user",
                              null=True, blank=True, on_delete=models.SET_NULL)
    code = models.CharField(verbose_name="Code", null=True, blank=True, max_length=64)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("EID")

    def __str__(self):
        return self.name


class EquipmentType(models.Model):
    etid = models.CharField(verbose_name="ETID", primary_key=True, max_length=48)
    name = models.CharField(verbose_name="Type Name", max_length=32)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("ETID")

    def __str__(self):
        return self.name
