from functools import wraps
from typing import List
import logging
import re
import hmac
import base64
import hashlib
from django.http import HttpRequest,HttpResponse,Http404,request
#from django.core.handlers.wsgi.WSGIRequest import GET
from .config import SHOPIFY_API_KEY,SERVER_HOST_NAME,APP_NAME,SHOPIFY_API_SECRET_KEY

#SERVER_BASE_URL = f"https://{SERVER_HOST_NAME}"
#INSTALL_REDIRECT_URL = f"{SERVER_BASE_URL}/app_installed"
#WEBHOOK_APP_UNINSTALL_URL = f"https://{SERVER_HOST_NAME}/app_uninstall"

def generate_install_redirect_url(shop:str,scopes:List,nonce:str, access_mode:List):
    INSTALL_REDIRECT_URL = f"https://{SERVER_HOST_NAME}/app_installed"
    scope_string = ','.join(scopes)
    access_mode_string = ','.join(access_mode)
    redirect_url = f"https://{shop}/admin/oauth/authorize?client_id={SHOPIFY_API_KEY}&scope={scope_string}&redirect_uri={INSTALL_REDIRECT_URL}&state={nonce}&grant_options[]={access_mode_string}"
    return redirect_url

def generate_post_install_redirect_url(shop:str):
    #Include the server host name here with the redirect to read the data
    redirect_url = f"https://{SERVER_HOST_NAME}/dataprocess"
    return redirect_url

def verify_hmac(data:bytes,orig_hmac:str)->bool:
    new_hmac= hmac.new(
        SHOPIFY_API_SECRET_KEY.encode('utf-8'),
        data,
        hashlib.sha256
    )
    return new_hmac.hexdigest() == orig_hmac

def is_valid_shop(shop:str)-> bool:
    shopname_regex = r'[a-zA-Z0-9][a-zA-Z0-9\-]*\.myshopify\.com[\/]?'
    return re.match(shopname_regex,shop)
