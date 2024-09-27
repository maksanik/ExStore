from django.db import models
from django.contrib.auth.models import AbstractUser
from goods.models import Product

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name="Аватар")
    
    def __str__(self):
        return self.username

class Cart_item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users') 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    count = models.PositiveIntegerField(default=1)
    
    class Meta:
        unique_together = ('user', 'product')
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ["-time_update"]
        
    def __str__(self):
        return f"{self.user} - {self.count} {self.product}"


# Create your models here.
