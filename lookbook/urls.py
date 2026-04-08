<<<<<<< HEAD
# lookbook/urls.py
=======
>>>>>>> 0f83cef365a9ee6e8294d229fd89b0bdb5e5e39b
from django.urls import path
from . import views

app_name = 'lookbook'

urlpatterns = [
<<<<<<< HEAD
    # Страница списка образов: /lookbook/
    path('', views.lookbook_list, name='lookbook_list'),
    
    # Детальная страница образа: /lookbook/1/
=======
    path('', views.lookbook_list, name='lookbook_list'),
>>>>>>> 0f83cef365a9ee6e8294d229fd89b0bdb5e5e39b
    path('<int:id>/', views.lookbook_detail, name='lookbook_detail'),
]