from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from order.models import Order
import chapa
from chapa import Chapa, WEBHOOK_EVENT, WEBHOOKS_EVENT_DESCRIPTION
from . utils import get_transaction_number
from django.contrib.auth.decorators import login_required


chapaAPP = Chapa(settings.CHAPA_SECRET)

@login_required(login_url="account_login")
def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        success_url = request.build_absolute_uri(reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:canceled'))
        transaction_id = get_transaction_number()
        data = {
                "email":order.email,
                "amount" :order.get_total_cost(),
                "first_name":order.first_name,
                "last_name":order.last_name,
                "tx_ref":transaction_id,
                "callback_url":"https://127.0.0.1:1200/",
                "return_url":success_url,
                "customization":{
                    "title" : "Woozie Checkout",
                    "description" :"You are paying to checkout a product from woozie"
                }
            }
        
        response = chapaAPP.initialize(**data)
        chapaAPP.verify(transaction_id)
        return redirect(response["data"].get("checkout_url"))

    return render(request, 'payment/payment_process.html', {"order" : order})

@login_required(login_url="account_login")
def payment_completed(request):
        return render(request, 'payment/payment_completed.html')

@login_required(login_url="account_login")
def payment_canceled(request):
        return render(request, 'payment/payment_canceled.html')

@login_required(login_url="account_login")
def payment_list(request):
    return render(request, "payment/payment_list.html")