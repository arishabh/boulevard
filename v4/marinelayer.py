from shopify import Shopify

NAME = 'marinelayer'
DISPLAY_NAME = 'Marine Layer'
cats = ['best-sellers-guys', 'guys-new', 'guys-buttondowns', 'guys-tees-basics', 'guys-henleys-polos', 'guys-bottoms', 'guys-outerwear', 'guys-sweaters', 'weekend-sport-guys', 'guys-boxers-socks', 'loungewear-guys', 'guys-last-call', 'guys-sunglasses-and-hats', 'home-accessories-guys', 'ml-masks']
cat_names = ['Best Sellers', 'New Arrivals', 'Buttondowns', 'Tees + Graphics', 'Henelys + Raglans', 'Bottoms', 'Hoodies + Outerwear', 'Sweaters', 'Boxers + Socks']
shipping = 'Free returns and delivery. Refund will be available within 1-2 days. Follow instructions from app or website'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
