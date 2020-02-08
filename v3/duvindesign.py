from shopify import Shopify

NAME = 'duvindesign' 
DISPLAY_NAME = 'Duvin'
cats = ['long-sleeve-tees', 'buttonups', 't-shirt', 'shorts', 'outerwear', 'headwear', 'accessories']
shipping = 'Free shipping and returns for orders placed in the USA'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()