from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from order.models import Order
import chapa
from chapa import Chapa, WEBHOOK_EVENT, WEBHOOKS_EVENT_DESCRIPTION
from . utils import get_transaction_number
from django.contrib.auth.decorators import login_required
from . tasks import payment_done
chapaAPP = Chapa(settings.CHAPA_SECRET)

@login_required(login_url="account_login")
def payment_process(request, order_id=None):
    if order_id is None:
        order_id = request.session.get('order_id', None)

    order = get_object_or_404(Order, id=order_id)
    
    if request.method == "POST":
        
        if order_id is not None:
            order_id = request.session.get('order_id', None)
            order = get_object_or_404(Order, id=order_id)

        transaction_id = get_transaction_number(order_id)
        success_url = request.build_absolute_uri(reverse('payment:completed', kwargs={'tx_ref': transaction_id}))
        cancel_url = request.build_absolute_uri(reverse('payment:canceled',  kwargs={'tx_ref': transaction_id}))
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
def payment_completed(request, tx_ref):
    if request.method == "GET":
        tx_ref_list = tx_ref.split("-")
        order_id = tx_ref_list[-1]
        print(order_id)
        order = Order.objects.get(id=order_id)
        print(order)
        order.tx_ref = tx_ref
        order.paid = True
        order.save()
        payment_done.delay(order.id)
        return render(request, 'payment/payment_completed.html')

@login_required(login_url="account_login")
def payment_canceled(request, tx_ref):
    if request.method == "GET":
        tx_ref_list = tx_ref.split("-")
        order_id = tx_ref_list[-1]
        print(order_id)
        order = Order.objects.get(id=order_id)
        order.tx_ref = None
        order.paid = False
        order.save()
        return render(request, 'payment/payment_canceled.html')

@login_required(login_url="account_login")
def payment_list(request):
    return render(request, "payment/payment_list.html")