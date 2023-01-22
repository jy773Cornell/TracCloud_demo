from django.contrib import admin
from CHEMICAL.models import Chemical, ChemicalType, ChemicalUnit
from utils.UUIDGen import gen_uuid


class ChemicalAdmin(admin.ModelAdmin):
    list_display = ('chemid', 'user', 'trade_name', 'epa_reg_no', 'type', 'unit', 'is_active', 'create_time',)

    list_filter = ('type', 'is_active',)

    list_per_page = 10

    list_editable = ('is_active',)

    exclude = ["chemid"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cid = gen_uuid("ChemID")
        super().save_model(request, obj, form, change)


class ChemicalTypeAdmin(admin.ModelAdmin):
    list_display = ('chemtid', 'name', 'note', 'is_active', 'create_time',)

    list_filter = ('is_active',)

    list_per_page = 10

    list_editable = ('name', 'note', 'is_active',)

    exclude = ["chemtid"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.ccid = gen_uuid("ChemTID")
        super().save_model(request, obj, form, change)


class ChemicalUnitAdmin(admin.ModelAdmin):
    list_display = ('chemuid', 'unit', 'note', 'is_active', 'create_time',)

    list_filter = ('is_active',)

    list_per_page = 10

    list_editable = ('unit', 'note', 'is_active',)

    exclude = ["chemuid"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.clcid = gen_uuid("ChemUID")
        super().save_model(request, obj, form, change)


admin.site.register(Chemical, ChemicalAdmin)

admin.site.register(ChemicalType, ChemicalTypeAdmin)

admin.site.register(ChemicalUnit, ChemicalUnitAdmin)
