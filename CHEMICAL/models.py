from django.db import models
from utils.ModelManager import MyModelManager


class Chemical(models.Model):
    chemid = models.CharField(verbose_name="ChemID", primary_key=True, max_length=48)
    user = models.ForeignKey(verbose_name="User", to="USER.User", to_field="uid", related_name="chem_user",
                             null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(verbose_name="Chemical Type", to="ChemicalType", to_field="chemtid",
                             related_name="chem_type", null=True, blank=True, on_delete=models.SET_NULL)
    trade_name = models.CharField(verbose_name="Trade Name", max_length=128)
    epa_reg_no = models.CharField(verbose_name="EPA Registration No.", max_length=64)
    formulation = models.CharField(verbose_name="Formulation", max_length=128)
    active_ingredient = models.CharField(verbose_name="Active Ingredient", max_length=128)
    percent_ai = models.FloatField(verbose_name="Active Ingredient Percent")
    unit = models.ForeignKey(verbose_name="Application Unit", to="ChemicalUnit", to_field="chemuid",
                             related_name="chem_unit", null=True, blank=True, on_delete=models.SET_NULL)
    rei = models.FloatField(verbose_name="REI")
    phi = models.IntegerField(verbose_name="PHI")
    labeled_crops = models.CharField(verbose_name="Labeled Crops", null=True, blank=True, max_length=256)
    restricted_use = models.BooleanField(verbose_name="Is Active", default=False)
    label_image = models.CharField(verbose_name="Labeled Image", null=True, blank=True, max_length=128)
    imported_from = models.CharField(verbose_name="Imported From", null=True, blank=True, max_length=32)
    validated_by = models.CharField(verbose_name="Validated By", null=True, blank=True, max_length=32)
    entered_year = models.IntegerField(verbose_name="Entered Year", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("ChemID")

    def __str__(self):
        return self.trade_name


class ChemicalType(models.Model):
    chemtid = models.CharField(verbose_name="ChemTID", primary_key=True, max_length=48)
    name = models.CharField(verbose_name="Type Name", max_length=128)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("ChemTID")

    def __str__(self):
        return self.name


class ChemicalUnit(models.Model):
    chemuid = models.CharField(verbose_name="ChemUID", primary_key=True, max_length=48)
    unit = models.CharField(verbose_name="Unit", max_length=128)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("ChemUID")

    def __str__(self):
        return self.unit
