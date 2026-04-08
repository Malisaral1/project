<<<<<<< HEAD
# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cart, CartItem
from shop.models import Product

def get_or_create_cart(request):
    """Получить или создать корзину для текущей сессии"""
    cart_id = request.session.get('cart_id')
    
    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
            return cart
        except Cart.DoesNotExist:
            pass
    
    # Создаём новую корзину
    cart = Cart.objects.create()
    request.session['cart_id'] = cart.id
    return cart


def cart_detail(request):
    """Страница корзины"""
    cart = get_or_create_cart(request)
    # Важно: select_related для оптимизации запросов
    items = cart.items.select_related('product').all()
    
    return render(request, 'cart/detail.html', {
        'cart': cart,
        'items': items
    })


def cart_add(request, product_id):
    """Добавить товар в корзину"""
    if request.method == 'POST':
        cart = get_or_create_cart(request)
        product = get_object_or_404(Product, id=product_id)
        
        # Получаем размер из POST-запроса (если есть)
        size = request.POST.get('size', '')
        
        # Проверяем, есть ли уже такой товар в корзине
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            size=size,
            defaults={'quantity': 1}
        )
        
        if not created:
            # Если товар уже есть — увеличиваем количество
            cart_item.quantity += 1
            cart_item.save()
        
        messages.success(request, f'Товар "{product.name}" добавлен в корзину!')
    
    return redirect('cart:cart_detail')


def cart_remove(request, item_id):
    """Удалить товар из корзины"""
    cart = get_or_create_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    item.delete()
    
    messages.success(request, 'Товар удалён из корзины.')
    return redirect('cart:cart_detail')


def cart_update(request, item_id):
    """Обновить количество товара в корзине"""
    cart = get_or_create_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()
    
    return redirect('cart:cart_detail')


def cart_clear(request):
    """Очистить корзину"""
    cart = get_or_create_cart(request)
    cart.items.all().delete()
    
    messages.success(request, 'Корзина очищена.')
    return redirect('cart:cart_detail')
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 0f83cef365a9ee6e8294d229fd89b0bdb5e5e39b
