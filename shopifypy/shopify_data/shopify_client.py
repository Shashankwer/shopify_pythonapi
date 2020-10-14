import json
from typing import List
import logging
import requests
from requests.exceptions import HTTPError
from .config import SHOPIFY_API_SECRET_KEY,SHOPIFY_API_KEY
from .models import ProductImage,Product,ProductVariant,Collection,CollectionImage,Collect,Customer,ClientOrder,Order,OrderdiscountCode,OrderLineItem,OrderLineItem,OrderLocation,orderNote,orderTag,AbandonCart,AbandonCartLineItem,Address,Customer

SHOPIFY_API_VERSION='2020-01'
REQUEST_METHODS = {
    "GET":requests.get,
    "POST":requests.post,
    "PUT":requests.put,
    "DEL":requests.delete
}

class ShopifyStoreClient():
    def __init__(self,shop:str,access_token:str):
        self.shop = shop
        self.base_url = f"https://{shop}/admin/api/{SHOPIFY_API_VERSION}"
        self.access_token = access_token
    
    @staticmethod
    def authenticate(shop:str,code:str)->str:
        url = f"https://{shop}/admin/oauth/access_token"
        payload = {
            "client_id":SHOPIFY_API_KEY,
            "client_secret":SHOPIFY_API_SECRET_KEY,
            "code":code
        }
        try:
            response = requests.post(url,json=payload)
            response.raise_for_status()
            return response.json()['access_token']
        except HTTPError as ex:
            logging.exception(ex)
            return None
    
    def authenticate_shopify_call(self,call_path:str,method:str,params:dict=None,headers:dict={},payload:dict={})->dict:
        url =f"{self.base_url}{call_path}"
        request_func=REQUEST_METHODS[method]
        headers['X-SHOPIFY-Access-Token']=self.access_token
        try:
            response = request_func(url,params=params,json=payload,headers=headers)
            response.raise_for_status()
            #logging.debug(f"authenticated_shopify_call response:\n {json.dump(response.json(),indent=4)}")
            return response.json()
        except HTTPError as ex:
            logging.exception(ex)
            return None
    
    def get_shop(self)-> dict:
        call_path = 'shop.json'
        method = 'GET'
        shop_response = self.authenticate_shopify_call(call_path=call_path,method=method)
        if not shop_response:
            return None
        return shop_response['shop']

    def get_script_tags(self)-> List:
        call_path = 'script_tags.json'
        method = 'GET'
        script_tags_response = self.authenticate_shopify_call(call_path=call_path,method=method)
        if not script_tags_response:
            return None
        return script_tags_response['script_tag']
    
    def create_webhook(self,address:str,topic:str)->dict:
        call_path=f'webhooks.json'
        method='GET'
        webhook_count_response = self.authenticate_shopify_call(call_path=call_path,method=method)
        if not webhook_count_response:
            return None
        return webhook_count_response['count']
#Create code for mapping API to object type


