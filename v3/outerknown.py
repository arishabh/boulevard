from shopify import Shopify

NAME = 'outerknown'
DISPLAY_NAME = 'Outerknown'
cats = ['sea-jeans', 'shirts', 'short-sleeve-shirts', 't-shirts', 'graphic-tees', 'polos-henleys', 'pants', 'sweaters', 'sweatshirts', 'outerwear', 'trunks', 'shorts', 'mens-shoes', 'accessories']
shipping = 'Free standard shipping on orders over $100. Orders placed with standard shipping will arrive in 3-7 business days.'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()