from django import template

register = template.Library()

@register.simple_tag
def is_in_favorites(user, product):
    """Проверяет, есть ли товар в избранном у пользователя"""
    if not user.is_authenticated:
        return False
    return user.favorites.filter(product=product).exists()