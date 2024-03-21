
from django.urls import path
from.views import *

app_name = "cart"

urlpatterns = [
    path("", cart, name="cart" ),
    path("update-cart/", cart_add, name="update_cart" ),
    path("cart-remove/", cart_remove, name="cart_remove" ),
]