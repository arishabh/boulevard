from shopify import Shopify

WEB_NAME = 'oarsandalps'  # Website name
DISPLAY_NAME = 'Oars + Alps - Apparel'
cats = ['deo-face-body-swag']
cat_names = []
imgs = []
shipping = 'Free Gifts with Orders $30+ | Free Shipping $40+ | Always Free Returns'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.url[0] = 'https://www.oarsandalps.com/collections/'
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
