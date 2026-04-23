from django.shortcuts import render

def about_view(request):
    """Страница 'О нас'"""
    return render(request, 'pages/about.html')