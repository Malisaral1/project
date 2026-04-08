# lookbook/urls.py
from django.urls import path
from . import views

app_name = 'lookbook'

urlpatterns = [
    # Страница списка образов: /lookbook/
    path('', views.lookbook_list, name='lookbook_list'),
    
    # Детальная страница образа: /lookbook/1/
    path('<int:id>/', views.lookbook_detail, name='lookbook_detail'),
]