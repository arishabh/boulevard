from shopify import Shopify

NAME = 'twillory'
DISPLAY_NAME = 'Twillory - Apparel'
cats = ['shirts', 'performance', 'safecotton', 'untuckables', 'performance-pants', 'accessories', 'undertwills', 'socks', 'collar-stays', 'scarves', 'sunglasses', 'ties']
cat_names = ['All Shirts', 'Performance', 'SafeCotton', 'Untuck(able)', 'Pants', 'Accessories', 'underTwills']
shipping = 'Free US Shipping & Returns'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
