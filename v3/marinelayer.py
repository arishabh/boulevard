from shopify import Shopify

NAME = 'marinelayer'
DISPLAY_NAME = 'Marine Layer'
cats = ['guys-tees-basics', 'guys-henleys-polos', 'guys-buttondowns', 'guys-sweaters', 'guys-outerwear', 'guys-bottoms', 'weekend-sport-guys', 'loungewear-guys', 'guys-last-call', 'guys-boxers-socks', 'guys-sunglasses-and-hats', 'home-accessories-guys']
shipping = 'Free returns and delivery. Refund will be available within 1-2 days. Follow instructions from app or website'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()