from django.contrib import admin

from app_menu.models import MenuItem, Menu


# Register your models here.
class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    prepopulated_fields = {"slug": ["title"]}
    fields = ['title', 'slug', 'parent']


class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]


admin.site.register(Menu, MenuAdmin)
