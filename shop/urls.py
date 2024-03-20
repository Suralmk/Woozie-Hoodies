from django.urls import path, include
from.views import *

app_name = "shop"

urlpatterns = [
    path("", home, name="home" ),
    path("products/", product_list, name="products" ),
]