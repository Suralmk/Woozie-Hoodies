from django.urls import path
from .views import *
from . import webhooks
app_name = 'payment'

urlpatterns = [
    path('process/', payment_process, name='process'),
    path('completed/', payment_completed, name='completed'),
    path('canceled/', payment_canceled, name='canceled'),
    path('webhook', webhooks.chapa_webhook, name='webhook'),

    path("list/", payment_list, name="payment_list"),
]