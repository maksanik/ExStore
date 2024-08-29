from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
    path('logout/', views.registration, name="logout"),
    path('profile/', views.profile, name="profile"),
]
