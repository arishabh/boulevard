from shopify import Shopify

NAME = 'katinusa'
DISPLAY_NAME = 'Katin - Apparel'
cats = ['trunks-1', 'bottoms', 'tops', 'accessories']
cat_names = ['Trunks', 'Bottoms', 'Tops', 'Accessories']
shipping = 'For up to 30 days, we’ll gladly accept unworn, unwashed, or defective merchandise purchased on katinusa.com for return or exchange.'
note = 'Final Upload'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
