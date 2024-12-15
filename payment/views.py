from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from order.models import Order
from chapa import Chapa
from .utils import get_transaction_number
from django.contrib.auth.decorators import login_required
from .tasks import payment_done

chapaAPP = Chapa("CHASECK_TEST-Q4sSmSLwdw7FI4Lx0N5xbgsZuEB0QA0O")

@login_required(login_url="account_login")
def payment_process(request, order_id=None):
    order_obj_id = order_id or request.session.get('order_id')
    order = get_object_or_404(Order, id=order_obj_id)

    if request.method == "POST":
        try:
            transaction_id = get_transaction_number(order_obj_id)
            success_url = request.build_absolute_uri(reverse('payment:completed', kwargs={'tx_ref': transaction_id}))
            cancel_url = request.build_absolute_uri(reverse('payment:canceled', kwargs={'tx_ref': transaction_id}))

            response = chapaAPP.initialize(
                email=order.email,
                amount=order.get_total_cost(),
                first_name=order.first_name,
                last_name=order.last_name,
                tx_ref=transaction_id,
                callback_url="https://127.0.0.1:8000/",
                return_url=success_url,
                customization={
                    "title": "Woozie Checkout",
                    "description": "You are paying to checkout a product from woozie",
                },
            )

            #chapaAPP.verify(transaction_id)
            return redirect(response["data"]["checkout_url"])
        except Exception as e:
            print(e)

    return render(request, 'payment/payment_process.html', {"order": order})

@login_required(login_url="account_login")
def payment_completed(request, tx_ref):
    tx_ref_list = tx_ref.split("-")
    order_id = tx_ref_list[-1]
    order = get_object_or_404(Order, id=order_id)
    order.tx_ref = tx_ref
    order.paid = True
    order.save()
    payment_done.delay(order.id)
    return render(request, 'payment/payment_completed.html')

@login_required(login_url="account_login")
def payment_canceled(request, tx_ref):
    tx_ref_list = tx_ref.split("-")
    order_id = tx_ref_list[-1]
    order = get_object_or_404(Order, id=order_id)
    order.tx_ref = None
    order.paid = False
    order.save()
    return render(request, 'payment/payment_canceled.html')

@login_required(login_url="account_login")
def payment_list(request):
    return render(request, "payment/payment_list.html")
