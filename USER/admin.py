from django.contrib import admin
from USER.models import User, UserType
from utils.UUIDGen import gen_uuid


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('UTID', 'TypeName', 'InfoDataTable', 'Valid',)

    list_filter = ('Valid',)

    list_per_page = 10

    list_editable = ('TypeName', 'InfoDataTable', 'Valid',)

    exclude = ["UTID"]

    def save_model(self, request, obj, form, change):
        if not obj.UTID:
            obj.UTID = gen_uuid("UTID")
        super().save_model(request, obj, form, change)


admin.site.register(UserType, UserTypeAdmin)

admin.site.register(User)
