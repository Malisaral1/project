from django import template

register = template.Library()

@register.simple_tag
def is_look_favorited(user, look):
    """Безопасная проверка: есть ли образ в избранном"""
    if not user.is_authenticated:
        return False
    if not look or look == '':
        return False
    return user.favorite_looks.filter(look=look).exists()