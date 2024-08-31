from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from goods.models import Category, Product
from users.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
        

        return render(request, 'users/profile.html')

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
        
        
        return render(request, 'users/profile.html')

def logout(request):
    auth.logout(request)
    
    return HttpResponseRedirect(reverse('main:index'))
