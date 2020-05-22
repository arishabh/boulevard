from shopify import Shopify

WEB_NAME = 'oliversapparel' # Website name
DISPLAY_NAME = 'Olivers'
cats = ['pants', 'shorts', 'tees', 'midlayers']
cat_names = ['Pants', 'Shorts', 'Tees', 'Midlayers']
shipping = ' We offer returns using our label for an $8 fee deducted from your refund, or you can return using your own carrier or a refund to store credit for no charge. Returns and exchanges must be received in original, unused and unwashed condition. All returns must be postmarked within 60 days from order date to be eligible for a return.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.url = ['https://shop.' + WEB_NAME + '.com/collections/', '/products.json?limit=250&page=']
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
