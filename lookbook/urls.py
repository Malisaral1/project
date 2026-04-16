# lookbook/urls.py
from django.urls import path
from . import views

app_name = 'lookbook'

urlpatterns = [
    path('', views.lookbook_list, name='lookbook_list'),
    path('<slug:slug>/', views.lookbook_detail, name='lookbook_detail'),  # ← Важно для работы страницы образа
]