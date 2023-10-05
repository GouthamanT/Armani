import json
from django.http import JsonResponse, Http404
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Product, Cart
# Create your views here.

def getproduct(request, productId):
    product = get_object_or_404(Product, pk=productId)
    return render(request, 'home/productView.html', { 'product': product })

def cartView(request):
    try:
        data = Cart.objects.filter(user_id=request.user.id)
        return render(request, 'cart/cartView.html', { 'cartItems': data })
    except Cart.DoesNotExist:
        raise Http404

def addItem(request):
    if (request.method == 'POST'):
        if (request.user.is_authenticated):
            data = json.loads(request.body)
            if(Product.objects.filter(id=data['productId']).exists() and request.user.id):

                if(Cart.objects.filter(product_id=data['productId'], user_id=request.user.id).exists()):
                    messages.info(request, 'Product already added to the cart')
                    return JsonResponse({
                        'message': 'Product already added to the cart'
                    }, status = 200)
                else:
                    Cart.objects.create(product_id=data['productId'], user_id=request.user.id)
                    messages.info(request, 'Product added to the cart')
                    return JsonResponse({
                        'message': 'Product added to the cart'
                    }, status = 200)
        else:
            return JsonResponse({
                        'message': 'User not logged in'
                    }, status = 200)

def removeCartItem(request):
    if (request.method == 'POST'):
        data = json.loads(request.body)
        print(data['cartId'])
        cart_item = Cart.objects.filter(id=data['cartId'], user_id=request.user.id)
        if(cart_item):
            cart_item.delete()
            return JsonResponse({
                'message': 'Cart item removed',
            }, status=200)
        else:
            return JsonResponse({
                'message': 'Item does not exist'
            }, status=200)