import shopify
from creds import *

class Shopify:
    def __init__(self):
        self.shopify = shopify
        self.shopify.ShopifyResource.set_site(shop_url)
