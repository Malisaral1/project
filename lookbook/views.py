<<<<<<< HEAD
# lookbook/views.py
from django.shortcuts import render, get_object_or_404
from .models import LookbookItem

def lookbook_list(request):
    """Страница со списком всех образов"""
    items = LookbookItem.objects.filter(active=True)
    return render(request, 'lookbook/list.html', {'items': items})


def lookbook_detail(request, id):
    """Детальная страница образа с точками"""
    item = get_object_or_404(LookbookItem, id=id, active=True)
    hotspots = item.hotspot_set.select_related('product').all()
    products_in_lookbook = [hs.product for hs in hotspots]
    
    # === КОНВЕРТИРУЕМ КООРДИНАТЫ В СТРОКИ С ТОЧКОЙ ===
    hotspots_data = []
    for hs in hotspots:
        # Создаём словарь с координатами как строки с точкой
        hotspots_data.append({
            'id': hs.id,
            'product': hs.product,
            'x': str(float(str(hs.x_percent).replace(',', '.'))),
            'y': str(float(str(hs.y_percent).replace(',', '.'))),
        })  # ← Вот здесь была ошибка! Нужно } и )
    # ==================================================
    
    return render(request, 'lookbook/detail.html', {
        'item': item,
        'hotspots_data': hotspots_data,  # ← НОВАЯ ПЕРЕМЕННАЯ
        'products_in_lookbook': products_in_lookbook
=======
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import LookbookItem, Hotspot

def lookbook_list(request):
    """Страница со списком всех образов"""
    lookbooks = LookbookItem.objects.filter(active=True)
    return render(request, 'lookbook/list.html', {'lookbooks': lookbooks})

def lookbook_detail(request, id):
    """Детальная страница образа с кликабельными точками"""
    lookbook = get_object_or_404(LookbookItem, id=id, active=True)
    hotspots = Hotspot.objects.filter(lookbook_item=lookbook).select_related('product')
    
    # Готовим данные для JavaScript
    hotspots_data = []
    for hotspot in hotspots:
        hotspots_data.append({
            'id': hotspot.id,
            'x': hotspot.x_percent,
            'y': hotspot.y_percent,
            'product': {
                'id': hotspot.product.id,
                'name': hotspot.product.name,
                'price': str(hotspot.product.price),
                'image_url': hotspot.product.image.url if hotspot.product.image else '',
                'sizes': hotspot.product.sizes,
            }
        })
    
    # Список всех товаров в образе для боковой панели
    products_in_look = [h.product for h in hotspots]
    
    return render(request, 'lookbook/detail.html', {
        'lookbook': lookbook,
        'hotspots_data': hotspots_data,
        'products_in_look': products_in_look,
>>>>>>> 0f83cef365a9ee6e8294d229fd89b0bdb5e5e39b
    })