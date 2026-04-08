from django.db import models
from shop.models import Product

class LookbookItem(models.Model):
    title = models.CharField('Название образа', max_length=200)
    image = models.ImageField('Фото образа', upload_to='lookbook/%Y/%m/%d')
    description = models.TextField('Описание образа', blank=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    active = models.BooleanField('Активно', default=True)
    products = models.ManyToManyField(Product, through='Hotspot')
    
    class Meta:
        verbose_name = 'Образ'
        verbose_name_plural = 'Образы'
        ordering = ['-created']
    
    def __str__(self):
        return self.title

class Hotspot(models.Model):
    lookbook_item = models.ForeignKey(LookbookItem, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    x_percent = models.FloatField('Координата X (%)')
    y_percent = models.FloatField('Координата Y (%)')
    
    class Meta:
        verbose_name = 'Точка'
        verbose_name_plural = 'Точки'
        unique_together = ('lookbook_item', 'product')
    
    def __str__(self):
        return f'{self.product.name} на {self.lookbook_item.title}'