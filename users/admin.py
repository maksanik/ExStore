from django.contrib import admin
from users.models import User, Cart_item

admin.site.register(User)

@admin.register(Cart_item)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'count')
    pass
    
        
