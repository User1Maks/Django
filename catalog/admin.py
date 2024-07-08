from django.contrib import admin
from catalog.models import Category, Product, Blog, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name_category")
    list_filter = ("name_category",)
    search_fields = (
        "name_category",
        "description",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name_product", "price", "category")
    list_filter = ("name_product", "price", "category")
    search_fields = (
        "name_product",
        "description",
    )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "created_at", "view_counter")
    search_fields = (
        "title",
        "text",
    )
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "version_number", "name_version", "current_version")
