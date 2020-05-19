from shopify import Shopify

WEB_NAME = 'altamontapparel' # Website name
DISPLAY_NAME = 'Altamont'
cats = ['new-arrivals', 'denim', 'pants', 't-shirts', 'knits-button-ups', 'sweatshirts', 'jackets', 'accessories']
cat_names = ['New Arrivals', 'Denim', 'Pants', 'Tees', 'Knits & Wovens', 'Hoodies & Sweaters', 'Jackets', 'Accessories']
shipping = 'Free shipping on U.S. orders over $100. You can return unworn and unused clothes to our warehouse within 30 days from point of purchase for a refund or store credit.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
