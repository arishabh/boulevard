from shopify import Shopify

NAME = 'katinusa'
DISPLAY_NAME = 'Katin'
cats = ['tops', 'bottoms', 'trunks-1', 'knits', 'flannel', 'shirts', 'sweaters', 'jackets-1', 'shorts', 'pants', 'new-arrivals', 'accessories']
note = 'Added display name for vendor and collection'
shipping = 'For up to 30 days, we’ll gladly accept unworn, unwashed, or defective merchandise purchased on katinusa.com for return or exchange.'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()