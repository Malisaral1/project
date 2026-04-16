# orders/models.py
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    """Заказ пользователя"""
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('processing', 'В обработке'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменён'),
    ]
    
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50, blank=True)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=20)
    address = models.TextField('Адрес доставки')
    city = models.CharField('Город', max_length=50)
    postal_code = models.CharField('Индекс', max_length=10, blank=True)
    
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')
    total_amount = models.DecimalField('Общая сумма', max_digits=10, decimal_places=2, default=0)
    
    # Для анонимных пользователей (без регистрации)
    session_key = models.CharField('Ключ сессии', max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Заказ #{self.id} - {self.first_name} {self.last_name}'
    
    def get_total_amount(self):
        return sum(item.get_total_cost() for item in self.items.all())


class OrderItem(models.Model):
    """Товар в заказе"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_name = models.CharField('Название товара', max_length=200)
    product_price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    size = models.CharField('Размер', max_length=10, blank=True, null=True)
    quantity = models.PositiveIntegerField('Количество', default=1)
    image = models.CharField('Изображение', max_length=500, blank=True)
    
    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'
    
    def __str__(self):
        return f'{self.product_name} ({self.size}) × {self.quantity}'
    
    def get_total_cost(self):
        return self.product_price * self.quantity