from django.urls import path
from . import views

app_name = 'lookbook'

urlpatterns = [
    path('', views.lookbook_list, name='lookbook_list'),
    path('<int:id>/', views.lookbook_detail, name='lookbook_detail'),
]