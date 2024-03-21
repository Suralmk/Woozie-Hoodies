from django.shortcuts import render
from . models import Order, OrderItem
from .forms import CreateOrderForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid:
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item["product"],
                                         price=item["price"],
                                         quantity=item["quantity"])
            cart.clear()
            return render(request, "orders/order_created.html", {"order" : order})
    else:
            form = CreateOrderForm()
    return render(request, "orders/order_create.html" ,{"cart" : cart, "form" : form})