from shopify import Shopify

WEB_NAME = 'thenueco' # Website name
DISPLAY_NAME = 'Nue Co. - '
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
