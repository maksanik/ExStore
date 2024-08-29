from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Category, Product

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    
    context = {
        'categories': categories,
        'products': products,
    }    

    return render(request, 'main/index.html', context=context)
# Create your views here.
