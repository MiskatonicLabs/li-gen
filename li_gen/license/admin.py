from django.contrib import admin

from .models import Category, License


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }
