from django.shortcuts import render, redirect, reverse
from . models import Order, OrderItem
from .forms import CreateOrderForm
from cart.cart import Cart
from .tasks import order_created
from django.contrib.auth.decorators import login_required
from . utils import validate_phone_number
from django.contrib import messages
@login_required(login_url="account_login")
def order_create(request):
    cart = Cart(request)
    initial_data = {
         "first_name" : request.user.first_name,
         "last_name" : request.user.last_name,
         "email" : request.user.email
    }
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            if not  validate_phone_number(str(form.cleaned_data["phone_no"])):
                messages.error(request, "Please enter a valid phone number!")
                return render(request, "orders/order_create.html" ,{"cart" : cart, "form" : form})
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
            for item in cart:
                OrderItem.objects.create(order=event,
                                         product=item["product"],
                                         price=item["price"],
                                         quantity=item["quantity"])
            cart.clear()
            order_created.delay(event.id)
            request.session['order_id'] = event.id
            return redirect(reverse("payment:process"))
    else:
            form = CreateOrderForm(initial=initial_data)
    return render(request, "orders/order_create.html" ,{"cart" : cart, "form" : form})

def orders_list(request):
    orders = Order.objects.filter(owner=request.user)
    return render(request, "orders/orders_list.html", {"orders" : orders})