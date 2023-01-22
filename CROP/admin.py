from django.contrib import admin
from CROP.models import Crop, CropCategory, CropLifecycle, CropGrowthStage
from utils.UUIDGen import gen_uuid


class CropAdmin(admin.ModelAdmin):
    list_display = ('cid', 'user', 'name', 'category', 'lifecycle', 'growth_stage',
                    'variety_list', 'note', 'is_active', 'create_time',)

    list_filter = ('name', 'category', 'lifecycle', 'growth_stage', 'is_active',)

    list_per_page = 10

    list_editable = ('note', 'is_active',)

    exclude = ["cid"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cid = gen_uuid("CID")
        super().save_model(request, obj, form, change)


class CropCategoryAdmin(admin.ModelAdmin):
    list_display = ('ccid', 'name', 'note', 'is_active', 'create_time',)

    list_filter = ('is_active',)

    list_per_page = 10

    list_editable = ('name', 'note', 'is_active',)

    exclude = ["ccid"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.ccid = gen_uuid("CCID")
        super().save_model(request, obj, form, change)


class CropLifecycleAdmin(admin.ModelAdmin):
    list_display = ('clcid', 'name', 'note', 'is_active', 'create_time',)

    list_filter = ('is_active',)

    list_per_page = 10

    list_editable = ('name', 'note', 'is_active',)

    exclude = ["clcid"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.clcid = gen_uuid("CLCID")
        super().save_model(request, obj, form, change)


class CropGrowthStageAdmin(admin.ModelAdmin):
    list_display = ('cgsid', 'name', 'note', 'is_active', 'create_time',)

    list_filter = ('is_active',)

    list_per_page = 10

    list_editable = ('name', 'note', 'is_active',)

    exclude = ["cgsid"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cgsid = gen_uuid("CGSID")
        super().save_model(request, obj, form, change)


admin.site.register(Crop, CropAdmin)

admin.site.register(CropCategory, CropCategoryAdmin)

admin.site.register(CropLifecycle, CropLifecycleAdmin)

admin.site.register(CropGrowthStage, CropGrowthStageAdmin)
