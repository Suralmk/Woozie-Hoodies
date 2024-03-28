from django.shortcuts import render
from . models import Category, Product
from django.http import JsonResponse
import json
from django.utils.translation import activate
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
    context = {"single_product" : single_product, "products" : products}
    return render(request, "shop/product_detail.html",context )

def product_category(request, category_slug):
    products = Product.objects.filter(category__slug=category_slug)
    return render(request, "shop/product_category.html", {"products" : products})

def user_account(request):
    return render(request, "shop/user/account.html")

def search_view(request):
    if request.method == 'GET':
        query = request.GET["search"]
        products = Product.objects.filter(name__icontains=query)
        context = {
        "products" : products,
        'query': query,
        "title" : f"Search Result for {query}"
            }
        return render(request, 'shop/product_list.html', context)
    
def change_language(request):
    language = 'am'  
    activate(language)
