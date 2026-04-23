from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.favorites_list, name='list'),  # ← Добавили главную страницу списка
    path('add/<int:product_id>/', views.add_to_favorites, name='add'),
    path('remove/<int:product_id>/', views.remove_from_favorites, name='remove'),  # ← Оставили только один remove
]