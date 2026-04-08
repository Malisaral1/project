<<<<<<< HEAD
# shop/views.py
=======
>>>>>>> 0f83cef365a9ee6e8294d229fd89b0bdb5e5e39b
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
<<<<<<< HEAD
    """Список товаров с фильтрацией по категории"""
=======
    """
    Отображение списка товаров с фильтрацией по категориям
    """
>>>>>>> 0f83cef365a9ee6e8294d229fd89b0bdb5e5e39b
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
<<<<<<< HEAD
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, id, slug):
    """Детальная страница товара"""
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})
=======
    return render(request,
                 'shop/product/list.html',
                 {'category': category,
                  'categories': categories,
                  'products': products})

def product_detail(request, id, slug):
    """
    Отображение детальной страницы товара
    """
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                 'shop/product/detail.html',
                 {'product': product})
>>>>>>> 0f83cef365a9ee6e8294d229fd89b0bdb5e5e39b
