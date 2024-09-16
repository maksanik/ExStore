from django.contrib import admin
from users.models import User, Cart

admin.site.register(User)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'count')
    pass
    
        
