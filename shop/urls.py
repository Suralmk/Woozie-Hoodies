from django.urls import path, include
from.views import *

app_name = "shop"

urlpatterns = [
    path("", home, name="home" ),
    path("products/", product_list, name="products" ),
    path("products/<slug:product_slug>/", product_detail, name="product_detail" ),
    path("products/<slug:product_category>/", product_category, name="product_category"),
]