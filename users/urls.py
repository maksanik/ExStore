from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('cart/', views.cart, name="cart"),
    path('cart/update', views.cart_update_item, name="cart_update_item"),
    path('cart/delete', views.cart_delete_item, name="cart_delete_item"),
    path('sell/', views.sell_product, name="sell"),
]
