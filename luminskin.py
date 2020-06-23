from shopify import Shopify

WEB_NAME = 'luminskin' # Website name
DISPLAY_NAME = 'Lumin - Grooming'
cats = ['']
cat_names = []
imgs = []
shipping = 'We do not accept returns for free trial, bulk, or commitment plan orders. Orders must be returned within 30 days of the original delivery date, as stated by the tracking number. Returns processed after the 30 day window are not be eligible for a refund.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.url = ['https://www.' + WEB_NAME + '.com', '/products.json?limit=250&page=']
brand.link = brand.url[0]+'/'
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
