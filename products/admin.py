from django.contrib import admin
from .models import Category, Product, Cart
# Register your models here.


class CategoryResources(admin.ModelAdmin):
    list_display = [ 'id', 'title']
    exclude = [ 'createdat' ]

class ProductResources(admin.ModelAdmin):
    list_display = [ 'id', 'title', 'price', 'description', 'category' ]
    exclude = [ 'createdat' ]

class CartResources(admin.ModelAdmin):
    list_display = [ 'product', 'user' ]
    exclude = [ 'createdat' ]

admin.site.register(Category, CategoryResources)
admin.site.register(Product, ProductResources)
admin.site.register(Cart, CartResources)