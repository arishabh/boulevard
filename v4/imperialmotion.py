from shopify import Shopify

WEB_NAME = 'imperialmotion' # Website name
DISPLAY_NAME = 'Imperial Motion' 
cats = []
cat_names = []
shipping = 'Free shipping on orders over $50. Free returns and exchanges for unused and unworn clothes within 30 days.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
