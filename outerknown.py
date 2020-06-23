from shopify import Shopify

NAME = 'outerknown'
DISPLAY_NAME = 'Outerknown - Apparel'
cats = ['sweatshirts', 'shirts', 'sweaters', 'polos-henleys', 'outerwear', 't-shirts', 'pants', 'trunks', 'shorts', 'graphic-tees', 'short-sleeve-shirts', 'mens-shoes', 'accessories']
cat_names = ['Sweats + Hoodies', 'Long Sleeve Shirts', 'Sweaters', 'Polos + Henleys', 'Outerwear', 'Tees', 'Pants']
shipping = 'Free standard shipping on orders over $100. Orders placed with standard shipping will arrive in 3-7 business days.'
note = 'Final upload time'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
