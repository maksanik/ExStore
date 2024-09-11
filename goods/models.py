from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    
    @staticmethod
    def get_default_category():
        return Category.objects.get(name="Другое")

        
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET(Category.get_default_category),
        related_name='products'
    )
    
    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    image = models.ImageField(upload_to="goods_images")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='images')
    
    def __str__(self):
        return f"Image of {self.product.name}"