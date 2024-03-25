from django.shortcuts import render, redirect, reverse
from . models import Order, OrderItem
from .forms import CreateOrderForm
from cart.cart import Cart
from .tasks import order_created
from django.contrib.auth.decorators import login_required

@login_required(login_url="account_login")
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        print("---------------------")
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item["product"],
                                         price=item["price"],
                                         quantity=item["quantity"])
            cart.clear()
            order_created.delay(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse("payment:process"))
    else:
            form = CreateOrderForm()
    return render(request, "orders/order_create.html" ,{"cart" : cart, "form" : form})