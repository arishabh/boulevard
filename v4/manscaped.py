from shopify import Shopify

WEB_NAME = 'manscaped' # Website name
DISPLAY_NAME = 'Manscaped' 
cats = ['collection-all']
cat_names = []
imgs = []
shipping = 'All Company products carry a 30-day Gentlemen’s Agreement from date of receipt of goods. All returns must be in their original individual packaging. Refunds do not include the original cost for shipping and handling. Discounted items are final sale and are not eligible for return or exchange.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
