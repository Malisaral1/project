from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from lookbook.models import LookbookItem
from .models import FavoriteLook

@login_required
def add_to_favorites(request, look_id):
    look = get_object_or_404(LookbookItem, id=look_id)
    FavoriteLook.objects.get_or_create(user=request.user, look=look)
    messages.success(request, 'Образ добавлен в избранное')
    return redirect(request.META.get('HTTP_REFERER', 'lookbook:lookbook_list'))

@login_required
def remove_favorite_look(request, look_id):
    if request.method == 'POST':
        FavoriteLook.objects.filter(user=request.user, look_id=look_id).delete()
        messages.success(request, 'Образ удалён из избранного')
    return redirect('favorite_looks:list')

@login_required
def favorite_looks_list(request):
    # Добавлен фильтр user=request.user, чтобы видеть только своё
    favorite_looks = FavoriteLook.objects.filter(user=request.user).select_related('look')
    return render(request, 'favorite_looks/list.html', {
        'favorite_looks': favorite_looks
    })
    
