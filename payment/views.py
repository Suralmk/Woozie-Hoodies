from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from order.models import Order
from django_chapa import api
from django.http import HttpResponse

chapa_Key = settings.CHAPA_SECRET


def payment_process(request):
    chapa = api.ChapaAPI()

    # send erquest needs a transaction parameter
    print(chapa.send_request())
    # order_id = request.session.get('order_id', None)
    # order = get_object_or_404(Order, id=order_id)

    # if request.method == 'POST':
        # success_url = request.build_absolute_uri(reverse('payment:completed'))
        # cancel_url = request.build_absolute_uri(reverse('payment:canceled'))

        # chapa.send_request()
        # chapa_data = {
        #     'amount': 1000,
        #     'currency': "ETB",
        #     'email': "sura@gmail.com",
        #     'first_name': "Surafel",
        #     'last_name': "Melaku",
        #     'tx_ref': "dsafafa",
        #     'phone_number': "",
        #     'customization[title]': "Woozie Pay ",
        #     'customization[description]': "Payment for woozie",
        #     "return_url": "https://www.google.com/"
        # # }
        # return HttpResponse("Works")
    return HttpResponse("Works")