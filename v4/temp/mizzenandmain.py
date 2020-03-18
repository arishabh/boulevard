from shopify import Shopify

NAME = 'mizzenandmain'
DISPLAY_NAME = 'Mizzen+Main'
cats = ['new-arrivals', 'best-sellers', 'leeward-blue-label', 'leeward-collection', 'cunningham-collection', 'tux-shirt', 'trim-sizes', 'classic-sizes', 'tall-collection', 'casual-sportshirts-2', 'flannels', 'short-sleeves', 'luxe-tee', 'blazer-navy-blue', 'pullovers', 'vests', 'phil-mickelson-golf-polos', 'baron-performance-chino', 'last-chance']
shipping = 'Free shipping and returns on orders above $100. Returns are eligible for unworn and unashed clothes within 30 days for a full refund.'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()