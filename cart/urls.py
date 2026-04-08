<<<<<<< HEAD
# cart/urls.py
=======
>>>>>>> 0f83cef365a9ee6e8294d229fd89b0bdb5e5e39b
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
<<<<<<< HEAD
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    path('update/<int:item_id>/', views.cart_update, name='cart_update'),
    path('clear/', views.cart_clear, name='cart_clear'),
=======
    # Пока пусто, позже добавим
>>>>>>> 0f83cef365a9ee6e8294d229fd89b0bdb5e5e39b
]