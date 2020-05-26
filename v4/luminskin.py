from shopify import Shopify

WEB_NAME = 'luminskin' # Website name
DISPLAY_NAME = 'Lumin' 
cats = []
cat_names = []
imgs = []
shipping = ''
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
