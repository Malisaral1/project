<<<<<<< HEAD
# config/urls.py
=======
>>>>>>> 0f83cef365a9ee6e8294d229fd89b0bdb5e5e39b
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
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
=======

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('lookbook/', include('lookbook.urls')),  # ← ЭТА СТРОКА ДОЛЖНА БЫТЬ
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 0f83cef365a9ee6e8294d229fd89b0bdb5e5e39b
