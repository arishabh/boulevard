from shopify import Shopify

WEB_NAME = 'magicmind' # Website name
DISPLAY_NAME = 'Magic mind' 
cats = ['']
cat_names = []
imgs = []
shipping = ''
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.url[0] = 'https://magicmind.co'
brand.link = brand.url[0]+'/'
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
