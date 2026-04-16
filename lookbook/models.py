from django.db import models
from shop.models import Product

class LookbookItem(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='lookbook/%Y/%m/%d')
    description = models.TextField(blank=True)
    products = models.ManyToManyField(Product, through='Hotspot', related_name='lookbooks')
    created = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False, verbose_name='Главный образ')
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Образ'
        verbose_name_plural = 'Lookbook'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('lookbook:lookbook_detail', args=[self.slug])


class Hotspot(models.Model):
    lookbook = models.ForeignKey(
        LookbookItem, 
        on_delete=models.CASCADE, 
        related_name='hotspots'
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    position_x = models.FloatField(help_text='Позиция X в процентах (0-100)')
    position_y = models.FloatField(help_text='Позиция Y в процентах (0-100)')
    
    class Meta:
        ordering = ['position_y', 'position_x']
        verbose_name = 'Кликабельная точка'
        verbose_name_plural = 'Кликабельные точки'
    
    def __str__(self):
        return f'{self.lookbook.name} - {self.product.name}'