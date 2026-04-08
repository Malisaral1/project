# настроим админку, чтобы мы могли добавлять товары и образы (4-й этап плана).
from django.contrib import admin
from .models import LookbookItem, Hotspot

class HotspotInline(admin.TabularInline):
    """Встроенное редактирование точек на странице образа"""
    model = Hotspot
    extra = 1
    autocomplete_fields = ['product']  # Удобный поиск товаров

@admin.register(LookbookItem)
class LookbookItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'active']
    list_filter = ['active']
    inlines = [HotspotInline]  # Добавляем точки прямо в форму образа
    
@admin.register(Hotspot)
class HotspotAdmin(admin.ModelAdmin):
    list_display = ['lookbook_item', 'product', 'x_percent', 'y_percent']
    list_filter = ['lookbook_item']