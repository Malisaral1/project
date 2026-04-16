# shop/models.py
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category, 
        related_name='products', 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    composition = models.CharField(max_length=500, blank=True, verbose_name='Состав')
    care = models.CharField(max_length=500, blank=True, verbose_name='Уход')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
        ]
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, 
        related_name='images', 
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    is_main = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Image for {self.product.name}'


class ProductSize(models.Model):
    product = models.ForeignKey(
        Product, 
        related_name='sizes', 
        on_delete=models.CASCADE
    )
    size = models.CharField(max_length=10)
    stock = models.PositiveIntegerField(default=0)
    
    class Meta:
        unique_together = ['product', 'size']
    
    def __str__(self):
        return f'{self.product.name} - {self.size}'