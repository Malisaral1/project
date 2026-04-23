from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def register(request):
    """Регистрация нового пользователя"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('/')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    """Вход пользователя"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли!')
            
            # 🔥 НОВАЯ ЛОГИКА: если админ → в админку, иначе → в каталог
            if user.is_staff or user.is_superuser:
                return redirect('/admin/')
            
            return redirect('/')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    """Выход пользователя"""
    logout(request)
    messages.info(request, 'Вы вышли из системы')
    return redirect('shop:product_list')