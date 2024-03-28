from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from . cart import Cart
from shop.models import Product
# Create your views here.
@login_required(login_url="account_login")
def cart(request):
    return render(request, "cart/cart.html")

@require_POST
def update_cart(request):
    data = json.loads(request.body)
    print(data)
    return JsonResponse({"cart_number" : "5"}, safe=False)

@login_required(login_url="account_login")
@require_POST
def cart_add(request):
    cart = Cart(request)
    data = json.loads(request.body)
    product_id = data.get("productId")
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product,
        quantity=int(data.get('quantity')),
        override_quantity=data.get('override'))
    for item in cart:
        product = item["product"]
        if int(product.id) == int(product_id):
            item_price = item["total_price"]
    
    return JsonResponse(
        {"cart_number" : cart.__len__(),
         "total_price" : cart.get_total_price(),
         "item_price" : item_price
        },
            safe=False)

@require_POST
def cart_remove(request):
    cart = Cart(request)
    data = json.loads(request.body)
    product_id = data.get("productId")
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    response = {
        "cart_number" : cart.__len__(),
        "total_price" : cart.get_total_price()
    }
    return JsonResponse(response, safe=False)

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})