from django.urls import path
from . views import *

app_name = "orders"

urlpatterns = [
    path('create/', order_create, name="order_create"),
    path('list/', orders_list, name="orders_list"),
    path('download/<slug:order_id>/', orders_download, name="orders_download"),
]