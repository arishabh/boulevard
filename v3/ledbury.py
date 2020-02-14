from shopify import Shopify

NAME = 'ledbury'
DISPLAY_NAME = 'Ledbury'
cats = ['fall-collection', 'dress-shirts', 'business-casual', 'casual-sport', 'the-tuxedo-capsule', 'sunday-shirting', 'blazers', 'sweaters', 'pants', 'ties', 'cold-weather-accessories', 'collar-stays', 'cufflinks-studs', 'pocket-squares']
shipping = 'Free shipping and returns for all orders above $125'
note = 'Final upload'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()