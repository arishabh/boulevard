from shopify import Shopify

NAME = 'featsocks'
DISPLAY_NAME = 'Feat - Apparel'
cats = ['blanketblend', 'socks', 'crewnecks']
cat_names = ['BlanketBlend', 'Socks', 'Crewnecks']
shipping = 'Free shipping and returns for orders above $75'
note = 'HAS 12 PRODUCTS WITH EXACT SAME EVERYTHING EXCEPT FOR HANDLE!! MOTHAFUCKERS!!!'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)