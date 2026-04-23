from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

class Favorite(models.Model):
    """Связь: Пользователь <-> Товар (Избранное)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='in_favorites')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Нельзя добавить один товар дважды
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные товары'

    def __str__(self):
        return f'{self.user.username} -> {self.product.name}'