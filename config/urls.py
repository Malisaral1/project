# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# 🔽 ИМПОРТЫ ДЛЯ ВОССТАНОВЛЕНИЯ ПАРОЛЯ 🔽
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path('lookbook/', include('lookbook.urls', namespace='lookbook')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('accounts/', include('accounts.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('favorite-looks/', include('favorite_looks.urls')),
    path('', include('pages.urls', namespace='pages')), 

    
    # 1. Форма ввода Email
    path('accounts/password_reset/', 
         PasswordResetView.as_view(
             template_name='accounts/password_reset_form.html',
             email_template_name='accounts/password_reset_email.html',
             success_url='/accounts/password_reset/done/'
         ), name='password_reset'),
    
    # 2. Страница "Проверьте почту"
    path('accounts/password_reset/done/', 
         PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'
         ), name='password_reset_done'),
    
    # 3. Страница ввода нового пароля (переход по ссылке из письма)
    path('accounts/reset/<uidb64>/<token>/', 
         PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html',
             success_url='/accounts/reset/done/'
         ), name='password_reset_confirm'),
         
    # 4. Страница "Пароль успешно изменен"
    path('accounts/reset/done/', 
         PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'
         ), name='password_reset_complete'),
]

# Раздача медиа-файлов только в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)