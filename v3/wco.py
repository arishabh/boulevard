from shopify import Shopify

NAME = 'w-co'
DISPLAY_NAME = 'W Co.'
cats = ['outerwear', 't-shirts', 'accessories']
shipping = 'FREE SHIPPING ON ORDERS OVER $100 — FREE RETURNS — FREE EXCHANGES'.lower()
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()