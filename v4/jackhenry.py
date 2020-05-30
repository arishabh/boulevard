from shopify import Shopify

WEB_NAME = 'jackhenry' # Website name
DISPLAY_NAME = 'Jack Henry' 
cats = ['hair', 'face', 'body', 'kits']
cat_names = ['Hair', 'Face', 'Body', 'Kits']
imgs = []
shipping = 'Free shipping and free returns. Returns available for unworn and unused products.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.url[0] = 'https://jackhenry.co/collections/'
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
