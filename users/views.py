from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from goods.models import Category, Product
from users.models import Cart
from users.forms import UserLoginForm, UserRegisterForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth
from django.urls import reverse

def profile(request):
    if request.method == 'POST':
        action = request.POST.get("action")
        
        if action == "save":
            form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('user:profile'))
        elif action == "delete":
            request.user.delete()
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ProfileForm(instance=request.user)
        
    context = {
        'form': form
    }    

    return render(request, 'users/profile.html', context=context)

def cart(request):
    # categories = Category.objects.all()
    products = Product.objects.all()
    
    context = {
        'products': products
    }    

    return render(request, 'users/cart.html', context=context)

def sell_product(request):
    # categories = Category.objects.all()
    # products = Product.objects.all()
    
    context = {
    }    

    return render(request, 'users/sellProduct.html', context=context)

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
    else:
        form = UserRegisterForm()
    
    context = {
        "form": form,
        "form_name": "UserLoginForm"
    }  

    return render(request, 'main/index.html', context=context)

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
        
    else:
        form = UserRegisterForm()
        
    context = {
        "form": form,
        "form_name": "UserRegisterForm"
    }
        
    return render(request, 'main/index.html', context=context)

def logout(request):
    auth.logout(request)
    
    return HttpResponseRedirect(reverse('main:index'))
