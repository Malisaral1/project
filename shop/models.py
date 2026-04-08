from django.db import models
from django.urls import reverse

class Category(models.Model):
    """Категория товара (например, Верхняя одежда, Обувь)"""
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('URL', max_length=200, unique=True)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    # ЭТОТ МЕТОД НУЖНО ДОБАВИТЬ (5 шаг)
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    """Товар"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('URL', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='products/%Y/%m/%d')
    description = models.TextField('Описание', blank=True)
    composition = models.CharField('Состав', max_length=300, blank=True, help_text='Например: 100% хлопок')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    available = models.BooleanField('В наличии', default=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)
    
    # Варианты размеров (храним как JSON или можно сделать отдельную модель, пока упростим)
    sizes = models.JSONField('Доступные размеры', default=list, help_text='Введите список размеров, например: ["XS", "S", "M", "L"]')
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
        ]
    
    def __str__(self):
        return self.name
    
    # ЭТОТ МЕТОД НУЖНО ДОБАВИТЬ (5 шаг)
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])