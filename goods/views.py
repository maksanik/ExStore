from django.shortcuts import render, redirect
from django.http import HttpResponse
from goods.models import Category, Product
from users.models import Cart_item
from users.models import User

# Create your views here.
def product_page(request, product_slug):
    if request.method == 'POST':
        product = Product.objects.get(slug=request.POST.get("product_slug", None))
        curr_user = request.user
        
        cart_item, created = Cart_item.objects.get_or_create(
            user=curr_user,
            product=product
        )
        
        if not created:
            cart_item.count += 1 
            cart_item.save()
            
        return redirect("main:index")
    else:
        product = Product.objects.get(slug=product_slug)
        curr_user = request.user
        product_in_cart = Cart_item.objects.filter(product=product, user=curr_user).first()
        print(product_in_cart.count)

        context = {
            "product": product,
            "product_in_cart": product_in_cart
        }
        
        return render(request, 'goods/product.html', context=context)

    