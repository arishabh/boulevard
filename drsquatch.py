from shopify import Shopify

WEB_NAME = 'drsquatch' # Website name
DISPLAY_NAME = 'Dr. Squatch - Grooming'
cats = ['bar-soaps', 'hair-care', 'shower-boosters', 'soap-subscription', 'colognes', 'beard', 'shave', '4-pack-hand-sanitizer', 'bay-rum-candle', 'soap-subscription', 'bundles', 'best-sellers']
cat_names = ['Bar Soaps', 'Hair Care', 'Shower Boosters']
imgs = ['https://drive.google.com/uc?export=download&id=1hPXxkQATj_ojlSCQV6QivPH-wPLmD_6F',
 'https://drive.google.com/uc?export=download&id=1vjI_wUES6o72P8Y8Bc15lVtgG_1jVR6L',
 'https://drive.google.com/uc?export=download&id=1gcijig1_5MWyAy_b0OwHSuF65Dfl-aQZ',
 'https://drive.google.com/uc?export=download&id=1ZUPtzuqMN6dEkMqkmrvZrXkMlYUMkM4m']
shipping = 'Free shipping on shopping over $40'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
