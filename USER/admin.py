from django.contrib import admin
from USER.models import User, UserType, UserRelation, UserRelationType
from utils.UUIDGen import gen_uuid
from utils.encrypt import md5


class UserAdmin(admin.ModelAdmin):
    list_display = ('UID', 'Username', 'Type', 'BusinessName', 'RegistrationNo', 'RegExpireDate', 'AddedBy',
                    'SelfActivated', 'Valid',)

    list_filter = ('Type', 'SelfActivated', 'Valid',)

    list_per_page = 10

    list_editable = ('SelfActivated', 'Valid',)

    exclude = ["UID"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.UID = gen_uuid("UID")
            obj.Password = md5(form.instance.Password)
        super().save_model(request, obj, form, change)


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('UTID', 'TypeName', 'InfoDataTable', 'Valid',)

    list_filter = ('Valid',)

    list_per_page = 10

    list_editable = ('TypeName', 'InfoDataTable', 'Valid',)

    exclude = ["UTID"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.UTID = gen_uuid("UTID")
        super().save_model(request, obj, form, change)


class UserRelationAdmin(admin.ModelAdmin):
    list_display = ('URID', 'Requester', 'Provider', 'RelationType', 'AddedBy', 'Valid',)

    list_filter = ('RelationType', 'Valid',)

    list_per_page = 10

    list_editable = ('Valid',)

    exclude = ["URID"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.URID = gen_uuid("URID")
        super().save_model(request, obj, form, change)


class UserRelationTypeAdmin(admin.ModelAdmin):
    list_display = ('URTID', 'TypeName', 'Note', 'Valid',)

    list_filter = ('Valid',)

    list_per_page = 10

    list_editable = ('TypeName', 'Note', 'Valid',)

    exclude = ["URTID"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.URTID = gen_uuid("URTID")
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)

admin.site.register(UserType, UserTypeAdmin)

admin.site.register(UserRelation, UserRelationAdmin)

admin.site.register(UserRelationType, UserRelationTypeAdmin)
