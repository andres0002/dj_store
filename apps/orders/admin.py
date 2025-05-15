# py
# django
from django.contrib import admin
# third
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# own
from apps.orders.models import Orders, OrdersLine

# Register your models here.

class OrdersResource(resources.ModelResource):
    class Meta:
        model = Orders

class OrdersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'create_date', 'update_date')
    list_filter = ('user', 'create_date', 'update_date')
    readonly_fields = ('create_date', 'update_date')
    source_class = OrdersResource

class OrdersLineResource(resources.ModelResource):
    class Meta:
        model = OrdersLine

class OrdersLineAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'product', 'order', 'price', 'amount', 'total', 'create_date', 'update_date')
    list_filter = ('user', 'product', 'order', 'create_date', 'update_date')
    readonly_fields = ('price', 'total', 'create_date', 'update_date')
    source_class = OrdersLineResource

admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrdersLine, OrdersLineAdmin)

