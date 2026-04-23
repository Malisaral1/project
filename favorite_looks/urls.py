from django.urls import path
from . import views

app_name = 'favorite_looks'

urlpatterns = [
    path('', views.favorite_looks_list, name='list'),
    path('add/<int:look_id>/', views.add_to_favorites, name='add'),
    # ИСПРАВЛЕНО: было remove_from_favorites, стало remove_favorite_look
    path('remove/<int:look_id>/', views.remove_favorite_look, name='remove'), 
]