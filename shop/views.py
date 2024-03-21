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
    products = Product.objects.all()
    context = {
        "products" : products
    }
    return render(request, "shop/product_list.html", context)

def product_detail(request, product_slug):
    single_product = Product.objects.filter(slug=product_slug).first()
    products = Product.objects.all()
    return render(request, "shop/product_detail.html", {"single_product" : single_product, "products" : products})

def product_category(request, product_category):
    products = Product.objects.filter(category__slug=category)
    return render(request, "shop/product_category.html", {"products" : products})
