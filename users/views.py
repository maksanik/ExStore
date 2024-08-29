from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from goods.models import Category, Product
from users.forms import UserLoginForm
from django.contrib import auth
from django.urls import reverse

def profile(request):
    # categories = Category.objects.all()
    # products = Product.objects.all()
    
    context = {
    }    

    return render(request, 'users/profile.html', context=context)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            
            username = request.POST['username']
            password = request.POST['password']
            
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
        
        context = {
        }    

        return render(request, 'users/profile.html', context=context)

def registration(request):
    
    context = {
    }    

    return render(request, 'users/profile.html', context=context)

def logout(request):
    
    context = {
    }    

    return render(request, 'users/profile.html', context=context)
