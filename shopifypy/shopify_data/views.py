from django.shortcuts import render
import uuid
import os
import json
import logging
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect,Http404
from . import helpers
from .shopify_client import ShopifyStoreClient
#from django.http.HttpRequest import GET 
#from . import helpers
# Create your views here.
ACCESS_TOKEN = None
NOUNCE = None 
ACCESS_MODE = [] #defaults to offline access mode if left blank or omitted. 
SCOPES = ['read_products']

def validate_url(dic)->bool:
    hmac = dic.get('hmac')
    sorted(dic)
    data = '&'.join([f"{key}={value}" for key,value in dic.items() if key!='hmac']).encode('utf-8')
    if not helpers.verify_hmac(data,hmac):
        logging.error(f"HMAC could not be verified:\n\thmac {hmac}\n\tdata {data}")
        raise Http404("HMAC could not be verified")
    shop = dic.get('shop')
    if shop and not helpers.is_valid_shop(shop):
        logging.error(f"invalid shop name received")
        raise Http404("Invalid shop name")
    return True

def app_launched(request):
    validate_url(request.GET)
    shop = request.GET.get('shop')
    print(shop)
    global ACCESS_TOKEN,NONCE
    if ACCESS_TOKEN:
        return HttpResponse(f"Hello {shop}")        
        
    NONCE = uuid.uuid4().hex
    redirect_url = helpers.generate_install_redirect_url(shop=shop,scopes=SCOPES,nonce=NONCE,access_mode=ACCESS_MODE)
    print(redirect_url)
    return HttpResponseRedirect(redirect_url)

def app_installed(request):
    validate_url(request.GET)
    state=request.GET.get('state')
    global NONCE,ACCESS_TOKEN
    print(NONCE,state)
    if state!=NONCE:
        print('error')
        return "Invalid `state` received",400
    NONCE = None
    #getting the access token
    shop = request.GET.get('shop')
    code = request.GET.get('code')
    print(shop,code)
    ACCESS_TOKEN = ShopifyStoreClient.authenticate(shop=shop,code=code)
    shopify_client = ShopifyStoreClient(shop=shop,access_token=ACCESS_TOKEN)
    redirect_url = helpers.generate_post_install_redirect_url(shop=shop)
    return HttpResponseRedirect(redirect_url)

def dataprocess(request):
    return HttpResponse("<h1>Part 1 done!!</h1>")