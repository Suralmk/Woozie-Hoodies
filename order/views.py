from django.shortcuts import render, redirect, reverse, get_object_or_404
from . models import Order, OrderItem
from .forms import CreateOrderForm
from cart.cart import Cart
from .tasks import order_created, download_order
from django.contrib.auth.decorators import login_required
from . utils import validate_phone_number
from django.contrib import messages
from django.http import HttpResponse
import weasyprint
from django.template.loader import render_to_string
from django.conf import settings

@login_required(login_url="account_login")
def order_create(request):
    cart = Cart(request)
    if not cart:
        return redirect(reverse("shop:home")) 
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

def orders_download(request, order_id):
    pdf = download_order.delay(order_id)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{order_id}.pdf"'  
    return response

def order_delete(request, order_id):
    order = Order.objects.filter(id=order_id).delete()
    return redirect(reverse("orders:orders_list"))