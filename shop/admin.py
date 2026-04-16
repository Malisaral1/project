# shop/admin.py
from django.contrib import admin
from .models import Category, Product, ProductImage, ProductSize

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created']
    list_filter = ['available', 'created', 'category']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductSizeInline]