from django.shortcuts import render
from . models import Category, Product
from django.http import JsonResponse
import json
# Create your views here.

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        "categories" :categories,
        "products":products
    }
    return render(request, "shop/home.html", context)

def product_list(request):
    return render(request, "shop/product_list.html")

def product_detail(request):
    return render(request, "shop/product_detail.html")

