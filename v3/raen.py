from shopify import Shopify

NAME = 'raen'
DISPLAY_NAME = 'Raen'
cats = ['sunglasses']
shipping = 'FREE RETURNS + 2 DAY SHIPPING ON U.S. ORDERS $150+'.lower()
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()