from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Category, Product

def index(request):
    
    category_slug = request.GET.get("category", None)
    if category_slug == None:
         products = Product.objects.all()
    else:
        products = Product.objects.filter(category__slug=category_slug).order_by("-id")
    
    categories = Category.objects.all()
    products = products.order_by("-id")
    
    context = {
        'categories': categories,
        'products': products,
    }    

    return render(request, 'main/index.html', context=context)
# Create your views here.
