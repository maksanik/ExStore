from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Category

def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }    

    return render(request, 'main/base.html', context=context)
# Create your views here.
