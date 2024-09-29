import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from goods.models import Category, Product
from users.models import Cart_item
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
    if request.method == "GET":
        curr_user = request.user
        user_cart = Cart_item.objects.filter(user=curr_user)
        total_sum = sum([cart_item.product.price * cart_item.count for cart_item in user_cart])
        
        context = {
            'user_cart': user_cart,
            'total_sum': total_sum
        }    

        return render(request, 'users/cart.html', context=context)

def cart_delete_item(request):
    if request.method == "POST":
        cart_item_id = json.loads(request.body).get("cart_item_id")
        if cart_item_id:
            try:
                cart_item =  Cart_item.objects.get(id=cart_item_id)
                user_cart =  Cart_item.objects.filter(user=cart_item.user)
                cart_item.delete()
                total_sum = sum([cart_item.product.price * cart_item.count for cart_item in user_cart])
                
                return JsonResponse({'success': True, 'total_sum': total_sum})
            except Exception:
                return JsonResponse({'success': False})
    
    return JsonResponse({'success': False})   
 
def cart_update_item(request):
    if request.method == "POST":
        data = json.loads(request.body)
        cart_item_id = data.get("cart_item_id")
        if cart_item_id:
            try:
                cart_item =  Cart_item.objects.get(id=cart_item_id)
                user_cart =  Cart_item.objects.filter(user=cart_item.user)
                cart_item.count = data.get("new_count")
                cart_item.save()
                
                total_sum = sum([cart_item.product.price * cart_item.count for cart_item in user_cart])
                
                return JsonResponse({'success': True, 'total_sum': total_sum, 'item_total_price': int(cart_item.count) * int(cart_item.product.price)})
            except Exception:
                return JsonResponse({'success': False})
    
    return JsonResponse({'success': False})

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
