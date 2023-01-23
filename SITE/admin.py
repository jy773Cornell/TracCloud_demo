from django.contrib import admin
from SITE.models import Site, SiteType, SiteUnit, SiteVariety
from utils.UUIDGen import gen_uuid


class SiteAdmin(admin.ModelAdmin):
    list_display = ('sid', 'user', 'name', 'type', 'crop', 'variety',
                    'crop_year', 'size', 'size_unit', 'parent', 'is_active', 'create_time',)

    list_filter = ('type', 'crop', 'parent', 'is_active',)

    list_per_page = 10

    list_editable = ('is_active',)

    exclude = ["sid"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.sid = gen_uuid("SID")
        super().save_model(request, obj, form, change)


class SiteTypeAdmin(admin.ModelAdmin):
    list_display = ('stid', 'name', 'level', 'parent_type', 'is_active', 'create_time',)

    list_filter = ('level', 'is_active',)

    list_per_page = 10

    list_editable = ('name', 'is_active',)

    exclude = ["stid"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.stid = gen_uuid("STID")
        super().save_model(request, obj, form, change)


class SiteUnitAdmin(admin.ModelAdmin):
    list_display = ('suid', 'unit', 'is_active', 'create_time',)

    list_filter = ('is_active',)

    list_per_page = 10

    list_editable = ('unit', 'is_active',)

    exclude = ["suid"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.suid = gen_uuid("SUID")
        super().save_model(request, obj, form, change)


class SiteVarietyAdmin(admin.ModelAdmin):
    list_display = ('svid', 'name', 'is_active', 'create_time',)

    list_filter = ('is_active',)

    list_per_page = 10

    list_editable = ('name', 'is_active',)

    exclude = ["svid"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.svid = gen_uuid("SVID")
        super().save_model(request, obj, form, change)


admin.site.register(Site, SiteAdmin)

admin.site.register(SiteType, SiteTypeAdmin)

admin.site.register(SiteUnit, SiteUnitAdmin)

admin.site.register(SiteVariety, SiteVarietyAdmin)
