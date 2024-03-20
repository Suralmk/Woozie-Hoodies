from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
def cart(request):
    return render(request, "shop/cart.html")

def update_cart(request):
    data = json.loads(request.body)
    print(data)
    return JsonResponse({"message" : "this is json"}, safe=False)