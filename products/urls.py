from django.urls import path
from .views import getproduct, cartView, addItem, removeCartItem

urlpatterns = [
    path('<int:productId>', getproduct),
    path('addToCart', addItem),
    path('cart', cartView),
    path('removeItem', removeCartItem)
]
