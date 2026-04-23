from django.db import models
from django.contrib.auth.models import User
from lookbook.models import LookbookItem

class FavoriteLook(models.Model):
    """Избранные образы из lookbook"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_looks')
    look = models.ForeignKey(LookbookItem, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'look')
        verbose_name = 'Избранный образ'
        verbose_name_plural = 'Избранные образы'

    def __str__(self):
        return f'{self.user.username} -> {self.look.title}'