# accounts/middleware.py
class AdminRedirectMiddleware:
    """Перенаправляет админов в /admin/ после входа"""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Если пользователь только что вошёл и он админ
        if hasattr(request, 'session') and request.session.get('just_logged_in'):
            if request.user.is_staff or request.user.is_superuser:
                request.session.pop('just_logged_in', None)
                from django.shortcuts import redirect
                return redirect('/admin/')
        
        return response