# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from django.http import JsonResponse
import json

def cart_detail(request):
    """Страница корзины"""
    cart = request.session.get('cart', {})
    return render(request, 'cart/detail.html', {'cart': cart})

def cart_api(request):
    """API: Возвращает корзину в формате JSON"""
    cart = request.session.get('cart', {})
    return JsonResponse(cart)

def cart_add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        size = data.get('size')
        quantity = int(data.get('quantity', 1))
        
        product = get_object_or_404(Product, id=product_id)
        cart = request.session.get('cart', {})
        
        cart_key = f'{product_id}_{size}'
        if cart_key in cart:
            cart[cart_key]['quantity'] += quantity
        else:
            cart[cart_key] = {
                'product_id': product.id,
                'name': product.name,
                'price': str(product.price),
                'size': size,
                'quantity': quantity,
                'image': product.images.first().image.url if product.images.exists() else ''
            }
        
        request.session['cart'] = cart
        request.session.modified = True
        
        return JsonResponse({
            'success': True, 
            'cart_count': sum(item['quantity'] for item in cart.values())
        })

def cart_remove(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cart_key = data.get('cart_key')
        cart = request.session.get('cart', {})
        
        if cart_key in cart:
            del cart[cart_key]
            request.session['cart'] = cart
            request.session.modified = True
        
        return JsonResponse({'success': True})

def cart_update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cart_key = data.get('cart_key')
        quantity = int(data.get('quantity'))
        
        cart = request.session.get('cart', {})
        if cart_key in cart and quantity >= 1:
            cart[cart_key]['quantity'] = quantity
            request.session['cart'] = cart
            request.session.modified = True
        
        return JsonResponse({'success': True})
def add_lookbook_to_cart(request, slug):
    """Добавить весь образ с выбранными размерами"""
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)
    
    try:
        from lookbook.models import LookbookItem
        import json
        
        # Получаем данные из запроса
        data = json.loads(request.body)
        selected_sizes = data.get('sizes', {})  # Словарь {product_id: size}
        
        lookbook = get_object_or_404(LookbookItem, slug=slug)
        hotspots = lookbook.hotspots.select_related('product').all()
        
        cart = request.session.get('cart', {})
        items_added = 0
        
        for hotspot in hotspots:
            product = hotspot.product
            # ✅ Используем выбранный размер или дефолтный
            size = selected_sizes.get(str(product.id), '30 мл')
            cart_key = f'{product.id}_{size}'
            
            if cart_key in cart:
                cart[cart_key]['quantity'] += 1
            else:
                cart[cart_key] = {
                    'product_id': product.id,
                    'name': product.name,
                    'price': str(product.price),
                    'size': size,
                    'quantity': 1,
                    'image': product.images.first().image.url if product.images.exists() else ''
                }
            items_added += 1
        
        request.session['cart'] = cart
        request.session.modified = True
        
        return JsonResponse({
            'success': True,
            'cart_count': sum(item['quantity'] for item in cart.values()),
            'items_added': items_added
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'error': str(e)
        }, status=500)
