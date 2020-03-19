from shopify import Shopify

NAME = 'duvindesign' 
DISPLAY_NAME = 'Duvin'
cats = ['t-shirt', 'long-sleeve-tees', 'buttonups', 'shorts', 'outerwear', 'headwear', 'accessories', 'sale']
cat_names = ['Tees & Tanks', 'Long Sleave Tees', 'Buttonups', 'Shorts', 'Outerwear', 'Headwear', 'Accessories', 'Sale']
shipping = 'Free shipping and returns for orders placed in the USA'
note = 'Final Upload'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
