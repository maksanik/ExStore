from django.contrib import admin
from goods.models import Category, Product, ProductImage

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'time_create', 'time_update', 'category')
    readonly_fields = ('time_create', 'time_update')
    prepopulated_fields =   {'slug': ('name',)}
    
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
