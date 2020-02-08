from shopify import Shopify

NAME = 'twillory'
DISPLAY_NAME = 'Twillory'
cats = ['performance', 'safecotton', 'untuckables', 'performance-pants', 'undertwills', 'socks', 'collar-stays', 'bottle-opener-stays', 'scarves', 'twillory-hats', 'laundry-bag', 'sunglasses', 'ties', 'tie-bar']
shipping = 'Free US Shipping & Returns'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()