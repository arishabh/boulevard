from shopify import Shopify

WEB_NAME = 'oliversapparel' # Website name
DISPLAY_NAME = 'Olivers'
cats = ['pants', 'shorts', 'tees', 'midlayers']
cat_names = ['Pants', 'Shorts', 'Tees', 'Midlayers']
shipping = 'Return is eligible within 365 days of delivery'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.url = ['https://shop.' + WEB_NAME + '.com/collections/', '/products.json?limit=250&page=']
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
