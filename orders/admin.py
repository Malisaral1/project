# orders/admin.py
from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product_name', 'product_price', 'size', 'quantity', 'image']
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    inlines = [OrderItemInline]
    readonly_fields = ['total_amount', 'created_at', 'updated_at', 'session_key']
    
    fieldsets = (
        ('Клиент', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Доставка', {
            'fields': ('address', 'city', 'postal_code')
        }),
        ('Информация о заказе', {
            'fields': ('total_amount', 'status', 'session_key', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product_name', 'size', 'quantity', 'product_price']
    list_filter = ['order__status']