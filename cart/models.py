# cart/models.py
from django.db import models
from shop.models import Product
from django.core.validators import MinValueValidator

class Cart(models.Model):
    """Корзина пользователя (создаётся одна на сессию)"""
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
    
    def __str__(self):
        return f'Корзина #{self.id}'
    
    def get_total_price(self):
        """Общая сумма корзины"""
        return sum(item.get_total_cost() for item in self.items.all())
    
    def get_total_items(self):
        """Общее количество товаров в корзине"""
        return sum(item.quantity for item in self.items.all())


class CartItem(models.Model):
    """Товар в корзине"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    size = models.CharField('Размер', max_length=10, blank=True, null=True)
    quantity = models.PositiveIntegerField('Количество', default=1, 
                                           validators=[MinValueValidator(1)])
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
        unique_together = ('cart', 'product', 'size')  # Один товар с одним размером = одна строка
    
    def __str__(self):
        size_info = f' ({self.size})' if self.size else ''
        return f'{self.product.name}{size_info} × {self.quantity}'
    
    def get_total_cost(self):
        """Стоимость этой позиции (цена × количество)"""
        return self.product.price * self.quantity