from shopify import Shopify

NAME = 'raen'
DISPLAY_NAME = 'Raen - Apparel'
cats = ['sunglasses', 'eyeglasses']
shipping = 'Free returns + 2 day shipping on U.S. orders $150+'
note = 'Have to do collections by yourself'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
