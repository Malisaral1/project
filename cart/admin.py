# cart/admin.py
from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    """Товары внутри корзины (для просмотра в админке)"""
    model = CartItem
    extra = 0
    readonly_fields = ['product', 'size', 'quantity', 'get_total_cost']
    
    def has_add_permission(self, request, obj=None):
        return False  # Запрещаем добавление товаров прямо в админке корзины
    
    def has_delete_permission(self, request, obj=None):
        return True  # Но разрешаем удаление

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'get_total_items', 'get_total_price']
    list_filter = ['created_at']
    inlines = [CartItemInline]
    readonly_fields = ['created_at', 'updated_at']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'size', 'quantity', 'get_total_cost', 'created_at']
    list_filter = ['cart', 'product']


# Register your models here.

