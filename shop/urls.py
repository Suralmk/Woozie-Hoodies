from django.urls import path, include
from.views import *

app_name = "shop"

urlpatterns = [
    path("", home, name="home" ),
    path("products/", product_list, name="products" ),
    path("products/<slug:product_slug>/", product_detail, name="product_detail" ),
    path("category/<slug:category_slug>/", product_category, name="product_category"),
    path("account/", user_account, name="user_account"),
    path("search_view/", search_view, name="search_view"),
    path("change_language/", change_language, name="change_language"),
]