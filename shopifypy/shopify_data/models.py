from django.db import models
from django.db import models


class PriceRule(models.Model):
    allocation_method = models.CharField(max_length=20)
    created_at=models.DateField(required=False)
    updated_at = models.DateField(required=False)    
    customer_selection = models.CharField(max_length=200)
    ends_at = models.DateField(required=False)
    id = models.CharField(max_length=200,primary_key=True)
    once_per_customer = models.BooleanField(default=True)
    prerequisite_quantity_range = models.IntegerField(default=1)
    prerequisite_shipping_price_range = models.CharField(max_length=200,required=False)
    prerequisite_subtotal_range = models.FloatField(default=0.0)
    prerequisite_purchase = models.FloatField(default=0.0)
    starts_at = models.DateField(required=False)
    target_selection = models.CharField(max_length=200,required=False)
    target_type = models.CharField(max_length=200,required=False)
    title= models.CharField(max_length=200)
    usage_limit = models.IntegerField(default=10)

class PriceRuleSavedSearch(models.Model):
    price_rule = models.ForeignKey(PriceRule,on_delete=models.CASCADE)
    saved_search = models.CharField(max_length=200)


class DiscountCode(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    price_rule_id = models.CharField(max_length=200,required=False)
    code = models.CharField(max_length=200)
    useage_count = models.IntegerField(default=0)
    created_at = models.DateField(required=False)
    updated_at = models.DateField(required=False)

class MarketingEvents(models.Model):
    remote_id = models.CharField(max_length=200,required=False)
    event_type = models.CharField(max_length=100,required=False)
    marketing_channel = models.CharField(max_length=10,required=False)
    paid = models.CharField(maxlength=10,required=False)
    referrring_domain = models.CharField(max_length=1000,required=False)
    budget = models.IntegerField(default =0)
    currency = models.CharField(max_length=10,default='',required=False)
    budget_type = models.CharField(max_length=3,default='',required=False)
    started_at = models.DateField(required=False)
    scheduled_end_at = models.DateField(required=False)
    ended_at = models.DateField(required=False)
    utm_campaign = models.CharField(max_length=10,default='',required=False)
    utm_source = models.CharField(max_length=10,default='',required=False)
    utm_medium = models.CharField(max_length=10,default='',required=False)
    description = models.CharField(max_length=100,default='',required=False)
    manage_url = models.CharField(max_length=100,default='',required=False)
    preview_url = models.CharField(max_length=100,default='',required=False)
    marketing_source = models.CharField(max_length=100,default='',required=False)

class Address(models.Model):
    address_type = models.CharField(max_length=200,default='',required=False)
    address_id = models.CharField(max_length=200,default='',required=False)
    company =  models.CharField(max_length=200,default='',required=False)
    address1 =  models.CharField(max_length=200,default='',required=False)
    address2 =  models.CharField(max_length=200,default='',required=False)
    city =  models.CharField(max_length=400,default='',required=False)
    latitude = models.CharField(max_length=100,default='',required=False)
    longitutde  = models.CharField(max_length=100,default='',required=False)
    country =  models.CharField(max_length=400,default='',required=False)
    zipcode =  models.CharField(max_length=10,default='',required=False)
    default = models.BooleanField(default=False)
    province_code = models.CharField(max_length=30,default='',required=False)
    country_code = models.CharField(max_length=100,default='',required=False)
    first_name = models.CharField(max_length=1000,default='',required=False)
    last_name = models.CharField(max_length=1000,default='',required=False)
    billing_Address_type = models.CharField(max_length=20,default='',required=False)


class Customer(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    email = models.EmailField(required=False)
    accept_marketing = models.BooleanField(default=False)
    created_at = models.DateField(required=False)
    updated_at = models.DateField(required=False)
    first_name = models.CharField(max_length=200,default='',required=False)
    last_name = models.CharField(max_length=200,default='',required=False)
    order_count = models.IntegerField(default=0)
    state = models.CharField(max_length=100,default='',required=False)
    total_spent = models.IntegerField(default=0)
    last_order_id = models.CharField(max_length=200,default='',required=False)
    multi_pass_identifier = models.CharField(max_length=200,default='',required=False)
    tax_exempt=models.BooleanField(default=False)
    tags = models.CharField(max_length=1000)
    last_order_name = models.CharField(max_length=400,default='',required=False)
    currency = models.CharField(max_length=100,default='',required=False)
    marketing_optin_level = models.CharField(max_length=100,default='',required=False)
    customer_address = models.ManyToManyField(Address,on_delete=models.CASCADE)

class PrerequisiteCustomer(models.Model):
    price_rule_id = models.ForeignKey(PriceRule,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,on_delete =models.CASCADE)

class AbandonCart(models.Model):
    buyer_accepts_marketing=models.BooleanField(default=False)
    cart_token = models.CharField(max_length=100,default='',required=False)
    completed_at = models.DateField(required=False)
    created_at = models.DateField(required=False)
    customer_locale = models.CharField(max_length=10,default='',required=False)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    device_id = models.CharField(max_length=200,default='',required=False)
    gateway  = models.CharField(max_length=200,default='',required=False)
    id = models.CharField(max_length=200,primary_key=True)
    landing_site=models.CharField(max_length=400,default='',required=False)
    location = models.CharField(max_length=200,default='',required=False)
    note = models.CharField(max_length=100,default='',required=False)
    currency_code = models.CharField(max_length=6,default='',required=False)
    referring_site = models.CharField(max_length=400,default='',required=False)
    source_name = models.CharField(max_length=400,default='',required=False)
    subtotal_price = models.FloatField(default=0.0)
    tokens = models.CharField(max_length=200,default='',required=False)
    total_discount = models.FloatField(default=0.0)
    total_price = models.FloatField(default=0.0)
    total_weight = models.FloatField(default=0.0)
    updated_at = models.DateField(required=False)
    user_id = models.CharField(max_length=200,required=False, default='')


class Order(models.Model):
    app_id = models.CharField(max_length=200,required=False,default='')
    browser_ip = models.CharField(max_length=200,required=False,default='')
    buyer_accepts_marketing = models.BooleanField(default=False)
    cancel_reason = models.CharField(max_length=200,required=False,default='')
    cancelled_at = models.DateField(required=False)
    cart_token = models.CharField(max_length=200,required=False,default='')
    checkout_id = models.CharField(max_length=200,required=False,default='')
    closed_at = models.DateField(required=False)
    created_at = models.DateField(required=False)
    currency = models.CharField(max_length=6,required=False,default='')
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    customer_locale = models.CharField(max_length=20,required=False,default='')
    order_email = models.CharField(max_length=200,required=False,default='')
    order_financial_status = models.CharField(max_length=30,required=False,default='')
    fullfillment_status = models.CharField(max_length=200,required=False,default='')
    gateway = models.CharField(max_length=20,required=False,default='')
    id = models.CharField(max_length=200,primary_key=True)
    landing_site = models.CharField(max_length=200,required=False,default='')
    landing_site_ref = models.CharField(max_length=200,required=False,default='')    
    name = models.CharField(max_length=200,required=False,default='')
    notes = models.CharField(max_length=200,required=False,default='')
    number = models.IntegerField(default=0)
    order_number= models.IntegerField(default=0)
    payment_gateway = models.CharField(max_length=200,required=False,default='')
    presenment_currency = models.CharField(max_length=10,required=False,default='')
    referring_site = models.CharField(max_length=200,required=False,default='')
    source_name = models.CharField(max_length=200,required=False,default='')
    total_discount = models.FloatField(default=0.0)
    total_line_item_price = models.FloatField(default=0.0)
    total_price = models.FloatField(default=0.0)
    total_line_tax = models.FloatField(default=0.0)
    total_tip = models.FloatField(default=0.0)
    user_id = models.CharField(max_length=200,required=False,default='')
    update_at = models.DateField(required=False)
    total_weight = models.CharField(max_length=20,required=False,default='')

class ClientOrder(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    accept_language = models.CharField(max_length=60,required=False,default='')
    browser_height = models.CharField(max_length=200,required=False,default='')
    browser_width = models.CharField(max_length=200,required=False,default='')
    session_hash = models.CharField(max_length=200,required=False,default='')
    user_hash = models.CharField(max_length=200,required=False,default='')


class OrderdiscountCode(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,required=False)
    abandoncart_id = models.ForeignKey(AbandonCart,on_delete=models.CASCADE)    
    discount_codes = models.ForeignKey(DiscountCode,on_delete=models.CASCADE)
    discount_price = models.CharField(max_length=200,required=False,default='')
    discount_type  = models.CharField(max_length=200,required=False,default='')

class Collection(models.Model):
    body_html = models.CharField(max_length=2000,required=False,default='')
    handle = models.CharField(max_length=200,required=False,default='')
    id  = models.CharField(max_length=200,primary_key=True)
    published_at = models.DateField(required=False)
    published_scope = models.CharField(max_length=200,required=False,default='')
    sort_order = models.CharField(max_length=200,required=False,default='')
    title = models.CharField(max_length=200,default='')
    update_at = models.DateField(required=False)

class PriceRuleEntity(models.Model):
    price_rule_id = models.ForeignKey(PriceRule,on_delete=models.CASCADE)
    collection_id = models.ForeignKey(Collection,on_delete=models.CASCADE)

class Product(models.Model):
    body_html = models.CharField(max_length=2000,required=False,default='')
    handle = models.CharField(max_length=200,required=False,default='')
    id  = models.CharField(max_length=200,primary_key=True)
    option_1=models.CharField(max_length=200,default = '')
    option_2= models.CharField(max_length=200,default = '')
    option_3 = models.CharField(max_length=200,default = '')
    product_type = models.CharField(max_length=200,required=False,default='')
    published_scope = models.CharField(max_length=200,required=False,default='')
    status = models.CharField(max_length=100,required=False,default='')
    published_date = models.DateField(required=False)
    update_at = models.DateField(required=False)
    tags = models.CharField(max_length=200,required=False,default='')
    template_suffix = models.CharField(max_length=200,required=False,default='')
    title = models.CharField(max_length=200,required=False,default='')
    vendor = models.CharField(max_length=200,required=False,default='')

class PrerequisiteProducts(models.Model):
    pricerule_id = models.ForeignKey(PriceRule,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)


class PriceRuleProduct(models.Model):
    price_rule_id = models.ForeignKey(PriceRule,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)

class ProductImage(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    id = models.CharField(max_length=200,primary_key=True)
    position = models.IntegerField(default=-1)
    src = models.CharField(max_length=200,required=False,default='')
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    update_at = models.DateField(required=False)


class Collect(models.Model):
    collection_id = models.ForeignKey(Collection,on_delete=models.CASCADE)
    created_at = models.DateField(required=False)
    position = models.IntegerField(default=-1)
    product_id = models.ForeignKey(Product,on_delete=False)
    updated_at = models.DateField(required=False)


class CollectionImage(models.Model):
    collection_id = models.ForeignKey(Collection,on_delete=models.CASCADE)
    src = models.CharField(max_length=200,required=False,default='')
    alt = models.CharField(max_length=20,required=False,default='')
    created_at = models.DateField(required=False)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)


class OrderLocation(models.Model):
    lineitem_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    country_code = models.CharField(max_length=20,required=False,default='')
    province_code = models.CharField(max_length=20,required=False,default='')
    name = models.CharField(max_length=200,required=False,default='')
    address1 = models.CharField(max_length=200,required=False,default='')
    address2 = models.CharField(max_length=200,required=False,default='')
    city = models.CharField(max_length=20,required=False,default='')
    zip_code = models.CharField(max_length=20,required=False,default='')

class orderNote(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    note_name = models.CharField(max_length=20,required=False,default='')
    note_value = models.CharField(max_length=400,required=False,default='')

class orderTag(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=40,required=False,default='')
    
class ProductVariant(models.Model):
    barcode =  models.CharField(max_length=200,required=False,default='')
    compare_at_price = models.FloatField(default=0)
    fullfillment_service=  models.CharField(max_length=200,required=False,default='')
    grams =  models.FloatField(default=0.0)
    id = models.CharField(max_length=200,primary_key=True)
    image_id = models.ForeignKey(ProductImage,on_delete=models.CASCADE)
    inventory_item_id = models.CharField(max_length=200,required=False,default='')
    position =models.CharField(max_length=200,required=False,default='')
    sku = models.CharField(max_length=200,required=False,default='') 
    taxable = models.BooleanField(default=False)
    title = models.CharField(max_length=200,required=False,default='')
    updated_at = models.DateField(required=False)
    weight = models.FloatField(default=0.0)
    weight_unit = models.FloatField(max_length=10)        

class PrerequisiteVariants(models.Model):
    pricerule_id=models.ForeignKey(PriceRule,on_delete=models.CASCADE)
    varaint_id = models.ForeignKey(ProductVariant,on_delete=models.CASCADE)

class PriceProductVariant(models.Model):
    price_rule_id = models.ForeignKey(PriceRule,on_delete=models.CASCADE)
    product_variant_id = models.ForeignKey(ProductVariant,on_delete=models.CASCADE)


class AbandonCartLineItem(models.Model):
    abandon_cart_id = models.ForeignKey(AbandonCart,on_delete=models.CASCADE)
    fullfillment_service = models.CharField(max_length=200,required=False,default='')
    fullfillment_status = models.CharField(max_length=200,required=False,default='')
    required_shipping = models.BooleanField(default=False)
    sku = models.CharField(max_length=200,required=False,default='')
    title = models.CharField(max_length=200,required=False,default='')
    variant_id= models.ForeignKey(ProductVariant,on_delete=models.CASCADE)
    variant_title = models.CharField(max_length=200,required=False,default='')
    vendor = models.CharField(max_length=200,required=False,default='')
class OrderLineItem(models.Model):
    fullfilment_quantity=models.CharField(max_length=200,required=False,default='')
    fullfilmen_service = models.CharField(max_length=200,required=False,default='')
    fullfilment_status = models.CharField(max_length=20,required=False,default='')
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    variant_id = models.ForeignKey(ProductVariant,on_delete=models.CASCADE)
    vendor = models.CharField(max_length=200,required=False,default='')
    name = models.CharField(max_length=200,required=False,default='')
    gift_card = models.CharField(max_length=200,required=False,default='')
    properties = models.CharField(max_length=200,required=False,default='')
    taxable = models.BooleanField(default=False)
    tip_payment_gateway = models.CharField(max_length=20,required=False,default='')
    tip_payment_method = models.CharField(max_length=20,required=False,default='')
    total_discount_amount = models.FloatField(default=0.0)
    id = models.CharField(max_length=200,primary_key=True)