from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Category, Product
from main.utils import q_search

def index(request):
    
    category_slug = request.GET.get("category", None)
    query = request.GET.get("q", None)
    print(query)
    
    if category_slug == None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__slug=category_slug).order_by("-id")
        
    if query:
        products = q_search(products, query)
    
    categories = Category.objects.all()
    products = products.order_by("-id")
    
    context = {
        'categories': categories,
        'products': products,
    }    

    return render(request, 'main/index.html', context=context)
# Create your views here.
