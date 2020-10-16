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
"""
For the Shopify following are the different rules: 
<https://{shop}.myshopify.com/admin/api/{version}/products.json?page_info={page_info}&limit={limit}>; rel={next}, <https://{shop}.myshopify.com/admin/api/{version}/products.json?page_info={page_info}&limit={limit}>; rel={previous}

Shopify REST end points support the cursor based pagination. When one sends a request to on of these endpoints, the response body returns the first page of results. 
The reponse header returns a link to the next page and the previous page of results. 
One can use the link in the response header to iterate through the pages of results. 

The link header includes a rel parameter, where relation-types describe the relation of the link page to the current page of results. 
The value can either be previous or next. 

If one intial request does not return enough to generate an additional page of results.
The URL in the link header can include up tom 3 parameters: 
1.page_info: A unique ID used to access a certain page of results. The page_info parameter cant be modified and must be used exactly as it appears in the link header URL
2. limit: The maximum number of results to show on the page
3. fields: A comma-separated litst of which fields to show in the results. This parameter only works for some endpoints

A request that include the page_info parameter except for limit and fields (if it appears to the endpoints)
If we want the results to be only filtered by the other parameters. Then to include those paramters in the first request to make
Any request that sends the page parameter will return  an error

e.g. requesting only 3 products page per result

GET https://{shop}.myshopify.com/admin/api/2019-07/products.json?limit=3&collection_id=841564295
Response header: 
Link: "<https://{shop}.myshopify.com/admin/api/2019-07/products.json?page_info=hijgklmn&limit=3>; rel=next"
{
  "products": [
    {id: 1 ... },
    {id: 2 ... },
    {id: 3 ... }
  ],
}

Inorder to go to the next page of results one can make a request to the URL stored in the link header of the last response. 
GET https://{shop}.myshopify.com/admin/api/2019-07/products.json?page_info=hijgklmn&limit=3
Since it includes a page info we cannot add any additional fields apart limit. 
Link: "<https://{shop}.myshopify.com/admin/api/2019-07/products.json?page_info=abcdefg&limit=3>; rel=previous, <https://{shop}.myshopify.com/admin/api/2019-07/products.json?page_info=opqrstu&limit=3>; rel=next"
{
  "products": [
    {id: 4 ... },
    {id: 5 ... },
    {id: 6 ... }
  ],
}


"""

    def dataPushDiscountCode(self):


        DiscountCode()



