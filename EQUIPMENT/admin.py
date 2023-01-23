from django.contrib import admin
from EQUIPMENT.models import Equipment, EquipmentType
from utils.UUIDGen import gen_uuid


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('eid', 'user', 'name', 'type', 'owner', 'code', 'is_active', 'create_time',)

    list_filter = ('type', 'is_active',)

    list_per_page = 10

    list_editable = ('is_active',)

    exclude = ["eid"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.eid = gen_uuid("EID")
        super().save_model(request, obj, form, change)


class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ('etid', 'name', 'note', 'is_active', 'create_time',)

    list_filter = ('is_active',)

    list_per_page = 10

    list_editable = ('name', 'note', 'is_active',)

    exclude = ["etid"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.etid = gen_uuid("ETID")
        super().save_model(request, obj, form, change)


admin.site.register(Equipment, EquipmentAdmin)

admin.site.register(EquipmentType, EquipmentTypeAdmin)
