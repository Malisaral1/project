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
    })