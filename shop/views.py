# shop/views.py
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from lookbook.models import LookbookItem

def index(request):
    """Главная страница с баннером и превью образов"""
    featured_lookbooks = LookbookItem.objects.filter(is_featured=True)[:3]
    return render(request, 'shop/index.html', {
        'featured_lookbooks': featured_lookbooks
    })

def product_list(request, category_slug=None):
    """Страница каталога товаров"""
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Фильтрация по цене
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    
    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):
    """Страница отдельного товара"""
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})