from shopify import Shopify

WEB_NAME = 'drsquatch' # Website name
DISPLAY_NAME = 'Dr. Squatch' 
cats = ['soap-subscription', 'bar-soaps', 'hair-care', 'shower-boosters', 'colognes', 'beard', 'shave', '4-pack-hand-sanitizer', 'bay-rum-candle', 'soap-subscription', 'bundles', 'best-sellers']
cat_names = ['Bar Soaps', 'Hair Care', 'Shower Boosters']
imgs = []
shipping = 'Free shipping on shopping over $40'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
