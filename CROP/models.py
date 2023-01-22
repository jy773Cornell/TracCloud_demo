from django.db import models
from utils.ModelManager import MyModelManager


class Crop(models.Model):
    cid = models.CharField(verbose_name="CID", primary_key=True, max_length=48)
    user = models.ForeignKey(verbose_name="User", to="USER.User", to_field="uid", related_name="crop_user",
                             null=True, blank=True, on_delete=models.SET_NULL)

    crop_choices = (
        (1, "Apple"),
        (2, "Berry"),
        (3, "Cherry"),
        (4, "Grape"),
        (5, "Pear"),
        (6, "Stone Fruit"),
        (7, "Golf"),
        (8, "Ground"),
        (9, "Lawn"),
        (10, "Sod"),
    )
    name = models.SmallIntegerField(verbose_name="Crop Name", choices=crop_choices)

    category = models.ForeignKey(verbose_name="Category", to="CropCategory", to_field="ccid",
                                 related_name="crop_category", null=True, blank=True, on_delete=models.SET_NULL)
    lifecycle = models.ForeignKey(verbose_name="Lifecycle", to="CropLifecycle", to_field="clcid",
                                  related_name="crop_lifecycle", null=True, blank=True, on_delete=models.SET_NULL)
    growth_stage = models.ForeignKey(verbose_name="Grow Stage", to="CropGrowthStage", to_field="cgsid",
                                     related_name="crop_growth_stage", null=True, blank=True, on_delete=models.SET_NULL)
    variety_list = models.CharField(verbose_name="Variety List", max_length=256)
    note = models.TextField(verbose_name="Note", null=True, blank=True)

    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("CID")

    def __str__(self):
        return "{}: {}".format(self.name, self.variety_list)


class CropCategory(models.Model):
    ccid = models.CharField(verbose_name="CCID", primary_key=True, max_length=48)
    name = models.CharField(verbose_name="Category Name", max_length=128)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("CCID")

    def __str__(self):
        return self.name


class CropLifecycle(models.Model):
    clcid = models.CharField(verbose_name="CLCID", primary_key=True, max_length=48)
    name = models.CharField(verbose_name="Lifecycle Name", max_length=128)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("CLCID")

    def __str__(self):
        return self.name


class CropGrowthStage(models.Model):
    cgsid = models.CharField(verbose_name="CGSID", primary_key=True, max_length=48)
    name = models.CharField(verbose_name="Stage Name", max_length=128)
    note = models.TextField(verbose_name="Note", null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)
    create_time = models.DateTimeField(verbose_name="Create Time", auto_now=True)

    objects = MyModelManager()
    objects.prefix("CGSID")

    def __str__(self):
        return self.name
