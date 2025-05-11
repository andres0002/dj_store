# py
# django
from django.contrib import admin
# third
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# own
from apps.services.models import Services

# Register your models here.

class ServicesResource(resources.ModelResource):
    class Meta:
        model = Services

class ServicesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name','create_date','update_date')
    list_filter = ('create_date','update_date')
    readonly_fields = ('create_date','update_date')
    source_class = ServicesResource

admin.site.register(Services, ServicesAdmin)