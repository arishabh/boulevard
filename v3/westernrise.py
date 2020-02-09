from shopify import Shopify

NAME = 'westernrise'
DISPLAY_NAME = 'Western Rise'
cats = ['mens-shirts', 'mens-bottoms', 'outerwear', 'merino-wool', 'accessories', 'bundles']
shipping = 'Free shipping and return available for orders above $150. Returns will be eligible for full refund within 60 days of purchase'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()