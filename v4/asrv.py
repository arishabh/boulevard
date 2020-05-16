from shopify import Shopify

WEB_NAME = 'asrv' # Website name
DISPLAY_NAME = 'ASRV'
cats = ['latest-drops', 'spring-2020-collection', 'all-tops-1', 'tanks', 'short-sleeves', 'long-sleeves', 'hoodies-warm-ups', 'jackets', 'training-division', 'all-tops', 'shorts', 'bottoms', 'leggings', 'accessories', 'masks', 'bags-1', 'headwear', 'socks-underwear', 'jewelry', 'accessories', 'surplus-sale']
cat_names = ['Latest Drops', 'New Collection', 'Tops ', 'Tanks', 'Short Sleeves', 'Long Sleeves', 'Hoodies and Warm-Ups', 'Jackets and Vests', 'Training Division', 'Bottoms ', 'Shorts', 'Tech Joggers', 'Leggings', 'Accessories ', 'Masks', 'Bags', 'Hats and Headwear', 'Socks and Underwear', 'Jewelry', 'All Accessories', 'Surplus Sale']
shipping = 'You can return it for a Refund, Store Credit or Size Exchange within 14 days of receiving your order. We offer free returns for Store Credit and Size Exchanges. A small restocking fee will be applied to Returns.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
