from shopify import Shopify

NAME = 'ledbury'
DISPLAY_NAME = 'Ledbury - Apparel'
cats = ['new-shirts', 'dress-shirts', 'business-casual', 'casual-sport', 'sunday-shirting', 'all-clothing', 'blazers', 'sweaters', 'pants', 'ties', 'cold-weather-accessories', 'collar-stays', 'cufflinks-studs', 'pocket-squares', 'the-tuxedo-capsule']
cat_names = ['New Shirts', 'Dress Shirts', 'Busienss Casual', 'Casual + Sport', 'Sunday Shirting', 'All Clothing', 'Sports Coats', 'Sweaters + Knits', 'Pants']
shipping = 'Free shipping and returns for all orders above $125'
note = 'Final upload'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
