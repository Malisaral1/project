# orders/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderItem
from .forms import OrderForm
import json

def checkout(request):
    """Страница оформления заказа"""
    # Получаем корзину из сессии
    cart = request.session.get('cart', {})
    
    if not cart:
        messages.warning(request, 'Ваша корзина пуста')
        return redirect('shop:product_list')
    
    # Считаем общую сумму
    total = sum(float(item['price']) * item['quantity'] for item in cart.values())
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Создаём заказ
            order = form.save(commit=False)
            order.total_amount = total
            order.session_key = request.session.session_key
            if not order.session_key:
                request.session.create()
                order.session_key = request.session.session_key
            order.save()
            
            # Создаём товары заказа
            for item_key, item_data in cart.items():
                OrderItem.objects.create(
                    order=order,
                    product_name=item_data['name'],
                    product_price=float(item_data['price']),
                    size=item_data.get('size', ''),
                    quantity=item_data['quantity'],
                    image=item_data.get('image', '')
                )
            
            # Очищаем корзину
            request.session['cart'] = {}
            request.session.modified = True
            
            # Перенаправляем на страницу подтверждения
            return redirect('orders:order_success', order_id=order.id)
    else:
        form = OrderForm()
    
    return render(request, 'orders/checkout.html', {
        'form': form,
        'cart': cart,
        'total': total
    })


def order_success(request, order_id):
    """Страница успешного оформления заказа"""
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/success.html', {'order': order})