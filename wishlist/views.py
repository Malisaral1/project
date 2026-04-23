from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shop.models import Product
from .models import Favorite 
from django.http import JsonResponse

@login_required
def add_to_favorites(request, product_id):
    """Добавление товара в избранное"""
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)
    messages.success(request, 'Товар добавлен в избранное')
    return redirect(request.META.get('HTTP_REFERER', 'shop:product_list'))

@login_required
def remove_from_favorites(request, product_id):
    """Удаление товара из избранного"""
    Favorite.objects.filter(user=request.user, product_id=product_id).delete()
    messages.info(request, 'Товар удалён из избранного')
    return redirect(request.META.get('HTTP_REFERER', 'shop:product_list'))

@login_required
def favorites_list(request):
    """Страница списка избранных товаров"""
    favorites = Favorite.objects.filter(user=request.user).select_related('product')
    return render(request, 'wishlist/list.html', {'favorites': favorites})
@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)

    # 🔥 Если запрос пришёл через JavaScript (fetch)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'is_fav': True})

    messages.success(request, 'Товар добавлен в избранное')
    return redirect(request.META.get('HTTP_REFERER', 'shop:product_list'))

@login_required
def remove_from_favorites(request, product_id):
    Favorite.objects.filter(user=request.user, product_id=product_id).delete()
    
    # 🔥 AJAX-ответ для удаления
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'is_fav': False})

    messages.info(request, 'Товар удалён из избранного')
    return redirect(request.META.get('HTTP_REFERER', 'shop:product_list'))