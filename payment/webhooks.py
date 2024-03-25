import chapa, json
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


import hmac
import hashlib
import json

def verify_webhook(secret_key: str, body: dict, chapa_signature: str) -> bool:
    signature = hmac.new(secret_key.encode(), json.dumps(body).encode(), hashlib.sha256).hexdigest()
    print(signature)
    return signature == chapa_signature

@csrf_exempt
def chapa_webhook(request):
    if request.method == 'POST':
        
        print(settings.CHAPA_SECRET_HASH)
        ver = verify_webhook(secret_key=settings.CHAPA_SECRET_HASH,
                             body=request.body.decode(),
                             chapa_signature=request.headers.get("Chapa-Signature"))
        if ver:
            print("The web hook is recived")
        return HttpResponse(status=200)
    else:
        print(request)
        return HttpResponse(status=404)

