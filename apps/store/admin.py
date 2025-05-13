# py
# django
from django.contrib import admin
# third
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# own
from apps.store.models import CategoriesProduct, Products

# Register your models here.

class CategoriesProductResource(resources.ModelResource):
    class Meta:
        model = CategoriesProduct

class CategoriesProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name','condition','create_date','update_date')
    list_filter = ('condition','create_date','update_date')
    readonly_fields = ('create_date','update_date')
    source_class = CategoriesProduct

class ProductsResource(resources.ModelResource):
    class Meta:
        model = Products

class ProductsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name','category','price','available','amount','condition','create_date','update_date')
    list_filter = ('category','available','condition','create_date','update_date')
    readonly_fields = ('create_date','update_date')
    source_class = ProductsResource

admin.site.register(CategoriesProduct, CategoriesProductAdmin)
admin.site.register(Products, ProductsAdmin)
