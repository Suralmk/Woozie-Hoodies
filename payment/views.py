from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from order.models import Order
from chapa import Chapa
from django.http import HttpResponse
from . utils import get_transaction_number
chapa = Chapa(settings.CHAPA_SECRET)

def payment_process(request):
    # get payment details from order model
    # first_name, last_name, email, amount
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        success_url = request.build_absolute_uri(reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:canceled'))

        data = {
                "email":order.email,
                "amount" :order.get_total_cost(),
                "first_name":order.first_name,
                "last_name":order.last_name,
                "tx_ref":get_transaction_number(),
                "callback_url":"https://127.0.0.1:1200/",
                "return_url":success_url,
                "customization":{
                    "title" : "Woozie Checkout",
                    "description" :"You are paying to checkout a product from woozie"
                }
            }
        
        response = chapa.initialize(**data)
        print(response)
        return redirect(response["data"].get("checkout_url"))

    return render(request, 'payment/payment_process.html', {"order" : order})

def payment_completed(request):
        return render(request, 'payment/payment_completed.html')

def payment_canceled(request):
        return render(request, 'payment/payment_canceled.html')