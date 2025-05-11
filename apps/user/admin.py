# django
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
# third
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# own
from apps.user.models import Users

# Register your models here.

class UsersResource(resources.ModelResource):
    class Meta:
        model = Users

class UsersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('username', 'email', 'name', 'lastname')
    list_display = ('username', 'email', 'name', 'lastname', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    source_class = UsersResource

admin.site.register(Users, UsersAdmin)
admin.site.register(Permission)
admin.site.register(ContentType)