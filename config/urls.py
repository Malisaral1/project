# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Главная → Lookbook
    path('', RedirectView.as_view(url='/lookbook/', permanent=False)),
    
    # Lookbook
    path('lookbook/', include('lookbook.urls', namespace='lookbook')),
    
    # Shop (Каталог)
    path('catalog/', include('shop.urls', namespace='shop')),
    
    # Cart (Корзина) ← Добавьте эту строку
    path('cart/', include('cart.urls', namespace='cart')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)