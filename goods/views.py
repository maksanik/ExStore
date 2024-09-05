from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Category, Product

# Create your views here.
def product_page(request, product_slug):
    
    product = Product.objects.get(slug=product_slug)
    
    context = {
        "product": product
    }
    
    return render(request, 'goods/product.html', context=context)
    