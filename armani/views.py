from django.shortcuts import render
from products.models import Product 

def home_page(request):
    products = Product.objects.all()
    return render(request, 'home/viewAll.html', {'products' : products})
