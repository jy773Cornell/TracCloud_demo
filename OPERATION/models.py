from django.db import models
from utils.ModelManager import MyModelManager


class Operation(models.Model):
    opid = models.CharField(verbose_name="OPID", primary_key=True, max_length=48)
    user = models.ForeignKey(verbose_name="User", to="USER.User", to_field="uid", related_name="op_user",
                             null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(verbose_name="Operation Type", to="OperationType", to_field="optid",
                             related_name="op_type", null=True, blank=True, on_delete=models.SET_NULL)
    datetime = models.DateTimeField(verbose_name="Operation Datetime", auto_now=True)
    multiple_site = models.BooleanField(verbose_name="Multiple Site", default=False)

    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("OPID")

    def __str__(self):
        return self.opid


class OperationType(models.Model):
    optid = models.CharField(verbose_name="OPTID", primary_key=True, max_length=48)
    name = models.CharField(verbose_name="Type Name", max_length=128)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("OPTID")

    def __str__(self):
        return self.name


class OperationUnit(models.Model):
    opuid = models.CharField(verbose_name="OPUID", primary_key=True, max_length=48)
    unit = models.CharField(verbose_name="Unit", max_length=32)

    usage_choices = (
        (1, "Area"),
        (2, "Liquid"),
    )
    usage = models.SmallIntegerField(verbose_name="Usage", choices=usage_choices)

    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("OPUID")

    def __str__(self):
        return self.unit
