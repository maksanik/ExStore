from django.contrib import admin
from goods.models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields =   {'slug': ('name',)}

# admin.site.register(Category)
