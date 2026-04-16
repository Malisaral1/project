# lookbook/views.py
import json
from django.shortcuts import render, get_object_or_404
from .models import LookbookItem

def lookbook_list(request):
    lookbooks = LookbookItem.objects.all()
    featured = lookbooks.filter(is_featured=True).first()
    return render(request, 'lookbook/list.html', {
        'lookbooks': lookbooks,
        'featured': featured
    })

def lookbook_detail(request, slug):
    lookbook = get_object_or_404(LookbookItem, slug=slug)
    hotspots = lookbook.hotspots.select_related('product').all()
    return render(request, 'lookbook/detail.html', {
        'lookbook': lookbook,
        'hotspots': hotspots
    }) 
    
def lookbook_detail(request, slug):
    lookbook = get_object_or_404(LookbookItem, slug=slug)
    hotspots = lookbook.hotspots.select_related('product').prefetch_related('product__sizes').all()
    
    # Подготавливаем данные для JavaScript
    hotspots_data = []
    for hotspot in hotspots:
        sizes = list(hotspot.product.sizes.values_list('size', flat=True))
        if not sizes:  # Если нет размеров, берём из ProductSize
            sizes = ['30 мл']  # Или дефолтное значение
        
        hotspots_data.append({
            'product_id': hotspot.product.id,
            'product_name': hotspot.product.name,
            'product_price': str(hotspot.product.price),
            'product_image': hotspot.product.images.first().image.url if hotspot.product.images.exists() else '/static/images/no-image.jpg',
            'product_sizes': sizes,  # ✅ Реальные размеры из БД
            'position_x': float(hotspot.position_x) if hotspot.position_x else 50,
            'position_y': float(hotspot.position_y) if hotspot.position_y else 50,
        })
    
    return render(request, 'lookbook/detail.html', {
        'lookbook': lookbook,
        'hotspots': hotspots,
        'hotspots_json': json.dumps(hotspots_data),  # Передаём в шаблон
    })