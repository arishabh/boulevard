from shopify import Shopify

WEB_NAME = 'supply'  # Website name
DISPLAY_NAME = 'Supply'
cats = ['the-single-edge-starter-set', 'the-single-edge-razors', 'grooming-essentials', 'skincare', 'accesories']
cat_names = []
imgs = []
shipping = 'Free US shipping on any order of $35 or more. We offer a 60 Day Trial for all of our gear, which means you have 60 days to try it out, live with it, and love it. If at any point in the first 60 days you decide that you are not 100% satisfied with your new products, return them for a full refund—no questions asked. Our return policy is simple - love our products, or send them back.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.url[0] = 'https://www.supply.co/collections/'
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
