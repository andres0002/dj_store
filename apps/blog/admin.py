# django
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# third
# own
from apps.blog.models import Categories, Authors, Posts

# Register your models here.

class CategoriesResource(resources.ModelResource):
    class Meta:
        model = Categories

class CategoriesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    readonly_fields = ('create_date', 'update_date')
    list_display = ('name', 'condition', 'create_date', 'update_date')
    list_filter = ('condition', 'create_date', 'update_date')
    resource_class = CategoriesResource

class AuthorsResource(resources.ModelResource):
    class Meta:
        model = Authors

class AuthorsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name', 'lastname', 'email']
    readonly_fields = ('create_date', 'update_date')
    list_display = ('name', 'lastname', 'facebook', 'twitter', 'instagram', 'web', 'email', 'condition', 'create_date', 'update_date')
    list_filter = ('condition', 'create_date', 'update_date')
    resource_class = AuthorsResource

class PostsResource(resources.ModelResource):
    class Meta:
        model = Posts

class PostsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title', 'slug', 'description']
    readonly_fields = ('create_date', 'update_date')
    list_display = ('title', 'slug', 'description', 'author', 'get_categories', 'condition', 'create_date', 'update_date')
    list_filter = ('author', 'categories', 'condition', 'create_date', 'update_date')
    resource_class = PostsResource

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Posts, PostsAdmin)