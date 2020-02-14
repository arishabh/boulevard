from shopify import Shopify

NAME = 'w-co'
DISPLAY_NAME = 'W Co.'
cats = ['new-releases', 'outerwear', 't-shirts', 'accessories']
cat_names = ['New Releases', 'Outerwear', 'T-Shirts', 'Accessories']
shipping = 'FREE SHIPPING ON ORDERS OVER $100 — FREE RETURNS — FREE EXCHANGES'.lower()
note = 'Final upload'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.url = ['https://' + NAME + '.us/collections/', '/products.json?limit=250&page=']
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)