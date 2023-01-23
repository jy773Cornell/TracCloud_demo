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


class PurchaseRecord(models.Model):
    prid = models.CharField(verbose_name="PRID", primary_key=True, max_length=48)
    user = models.ForeignKey(verbose_name="User", to="USER.User", to_field="uid", related_name="pr_user",
                             null=True, blank=True, on_delete=models.SET_NULL)
    opid = models.ForeignKey(verbose_name="OPID", to="OPERATION.Operation", to_field="opid", related_name="pr_op",
                             null=True, blank=True, on_delete=models.SET_NULL)
    pur_datetime = models.DateTimeField(verbose_name="Purchase Datetime", null=True, blank=True)
    operator = models.ForeignKey(verbose_name="Operator", to="USER.User", to_field="uid", related_name="pr_op_user",
                                 null=True, blank=True, on_delete=models.SET_NULL)
    chemical = models.ForeignKey(verbose_name="Chemical", to="CHEMICAL.Chemical", to_field="chemid",
                                 related_name="pr_chem", null=True, blank=True, on_delete=models.SET_NULL)
    chemical_type = models.ForeignKey(verbose_name="Chemical Type", to="CHEMICAL.ChemicalType", to_field="chemtid",
                                      related_name="pr_chem_type", null=True, blank=True, on_delete=models.SET_NULL)
    vendor = models.CharField(verbose_name="Vendor", null=True, blank=True, max_length=128)
    amount = models.FloatField(verbose_name="Amount")
    cost_per_unit = models.FloatField(verbose_name="Cost Per Unit")
    total_cost = models.FloatField(verbose_name="Total Cost")
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("PRID")

    def __str__(self):
        return "{} ({})".format(self.chemical, self.pur_datetime)


class HarvestRecord(models.Model):
    hrid = models.CharField(verbose_name="HRID", primary_key=True, max_length=48)
    user = models.ForeignKey(verbose_name="User", to="USER.User", to_field="uid", related_name="hr_user",
                             null=True, blank=True, on_delete=models.SET_NULL)
    opid = models.ForeignKey(verbose_name="OPID", to="OPERATION.Operation", to_field="opid", related_name="hr_op",
                             null=True, blank=True, on_delete=models.SET_NULL)
    har_datetime = models.DateTimeField(verbose_name="Harvest Datetime", null=True, blank=True)
    operator = models.ForeignKey(verbose_name="Operator", to="USER.User", to_field="uid", related_name="hr_op_user",
                                 null=True, blank=True, on_delete=models.SET_NULL)
    crop = models.ForeignKey(verbose_name="Crop", to="CROP.Crop", to_field="cid", related_name="hr_crop",
                             null=True, blank=True, on_delete=models.SET_NULL)
    site = models.ForeignKey(verbose_name="Site", to="SITE.Site", to_field="sid", related_name="hr_site",
                             null=True, blank=True, on_delete=models.SET_NULL)
    planting_date = models.DateField(verbose_name="Planting Date", null=True, blank=True)
    bloom_date = models.DateField(verbose_name="Bloom Date", null=True, blank=True)
    hr_area = models.FloatField(verbose_name="Harvest Area")
    area_unit = models.ForeignKey(verbose_name="Area Unit", to="OPERATION.OperationUnit", to_field="opuid",
                                  related_name="hr_opu", null=True, blank=True, on_delete=models.SET_NULL)
    rows = models.IntegerField(verbose_name="Rows")
    tracing_no = models.CharField(verbose_name="Tracking No.", null=True, blank=True, max_length=128)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("HRID")

    def __str__(self):
        return "{} ({})".format(self.site, self.har_datetime)


class ApplicationRecord(models.Model):
    arid = models.CharField(verbose_name="ARID", primary_key=True, max_length=48)
    user = models.ForeignKey(verbose_name="User", to="USER.User", to_field="uid", related_name="ar_user",
                             null=True, blank=True, on_delete=models.SET_NULL)
    opid = models.ForeignKey(verbose_name="OPID", to="OPERATION.Operation", to_field="opid", related_name="ar_op",
                             null=True, blank=True, on_delete=models.SET_NULL)
    app_datetime = models.DateTimeField(verbose_name="Harvest Datetime", null=True, blank=True)
    operator = models.ForeignKey(verbose_name="Operator", to="USER.User", to_field="uid", related_name="ar_op_user",
                                 null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(verbose_name="Application Type", to="OPERATION.ApplicationType", to_field="atid",
                             related_name="ar_type", null=True, blank=True, on_delete=models.SET_NULL)
    chemical = models.ForeignKey(verbose_name="Chemical", to="CHEMICAL.Chemical", to_field="chemid",
                                 related_name="ar_chem", null=True, blank=True, on_delete=models.SET_NULL)
    chemical_type = models.ForeignKey(verbose_name="Chemical Type", to="CHEMICAL.ChemicalType", to_field="chemtid",
                                      related_name="ar_chem_type", null=True, blank=True, on_delete=models.SET_NULL)
    water_use = models.BooleanField(verbose_name="Water Use")
    water_unit = models.ForeignKey(verbose_name="Water Unit", to="OPERATION.OperationUnit", to_field="opuid",
                                   related_name="ar_water_opu", null=True, blank=True, on_delete=models.SET_NULL)
    application_rate = models.FloatField(verbose_name="Application Rate")
    rate_unit = models.ForeignKey(verbose_name="Rate Unit", to="OPERATION.OperationUnit", to_field="opuid",
                                  related_name="ar_rate_opu", null=True, blank=True, on_delete=models.SET_NULL)
    total_amount = models.FloatField(verbose_name="Total Amount")
    amount_unit = models.ForeignKey(verbose_name="Amount Unit", to="OPERATION.OperationUnit",
                                    to_field="opuid", related_name="ar_amount_opu", null=True, blank=True,
                                    on_delete=models.SET_NULL)
    total_cost = models.FloatField(verbose_name="Total Cost")
    site = models.ForeignKey(verbose_name="Site", to="SITE.Site", to_field="sid", related_name="ar_site",
                             null=True, blank=True, on_delete=models.SET_NULL)
    applied_area = models.FloatField(verbose_name="Applied Area")
    area_unit = models.ForeignKey(verbose_name="Amount Unit", to="OPERATION.OperationUnit",
                                  to_field="opuid", related_name="ar_area_opu", null=True, blank=True,
                                  on_delete=models.SET_NULL)
    crop = models.ForeignKey(verbose_name="Crop", to="CROP.Crop", to_field="cid", related_name="ar_crop",
                             null=True, blank=True, on_delete=models.SET_NULL)
    growth_stage = models.ForeignKey(verbose_name="Growth Stage", to="CROP.CropGrowthStage", to_field="cgsid",
                                     related_name="ar_growth_stage", null=True, blank=True, on_delete=models.SET_NULL)
    purpose = models.ForeignKey(verbose_name="Purpose", to="OPERATION.ApplicationPurpose", to_field="apid",
                                related_name="ar_purpose", null=True, blank=True, on_delete=models.SET_NULL)
    decision_support = models.ForeignKey(verbose_name="Decision Support", to="OPERATION.DecisionSupport",
                                         to_field="dsid", related_name="ar_decision_support", null=True, blank=True,
                                         on_delete=models.SET_NULL)
    decide_by = models.CharField(verbose_name="Decided By", null=True, blank=True, max_length=64)
    customer = models.ForeignKey(verbose_name="Customer", to="USER.User", to_field="uid",
                                 related_name="ar_customer_user", null=True, blank=True, on_delete=models.SET_NULL)
    wind_speed = models.FloatField(verbose_name="Wind Speed", null=True, blank=True)

    direction_choices = (
        ("1", "east"),
        ("2", "north"),
        ("3", "south"),
        ("4", "west"),
        ("5", "southwest"),
        ("6", "northwest"),
        ("7", "southeast"),
        ("8", "northeast"),
    )
    wind_direction = models.SmallIntegerField(verbose_name="Wind Direction", null=True, blank=True,
                                              choices=direction_choices)

    average_temp = models.FloatField(verbose_name="Average Temperature", null=True, blank=True)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("ARID")

    def __str__(self):
        return "{} ({})".format(self.site, self.app_datetime)


class ApplicationType(models.Model):
    atid = models.CharField(verbose_name="ATID", primary_key=True, max_length=48)
    name = models.CharField(verbose_name="Type Name", max_length=128)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("ATID")

    def __str__(self):
        return self.name


class ApplicationPurpose(models.Model):
    apid = models.CharField(verbose_name="APID", primary_key=True, max_length=48)
    name = models.CharField(verbose_name="Type Name", max_length=128)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("APID")

    def __str__(self):
        return self.name


class DecisionSupport(models.Model):
    dsid = models.CharField(verbose_name="DSID", primary_key=True, max_length=48)
    name = models.CharField(verbose_name="Type Name", max_length=128)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("DSID")

    def __str__(self):
        return self.name
