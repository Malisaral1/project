# lookbook/admin.py
from django.contrib import admin
from .models import LookbookItem, Hotspot

class HotspotInline(admin.TabularInline):
    model = Hotspot
    extra = 1
    raw_id_fields = ['product']

@admin.register(LookbookItem)
class LookbookItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_featured', 'created']
    list_filter = ['is_featured', 'created']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [HotspotInline]

@admin.register(Hotspot)
class HotspotAdmin(admin.ModelAdmin):
    list_display = ['lookbook', 'product', 'position_x', 'position_y']
    list_filter = ['lookbook']
    raw_id_fields = ['product']