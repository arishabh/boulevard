from shopify import Shopify

WEB_NAME = 'coalatree' # Website name
DISPLAY_NAME = 'Coalatree' 
cats = ['mens-jackets', 'mens-sweatshirts-hoddies', 'mens-pants', 'mens-shorts', 'mens-tees', 'accessories']
cat_names = ['Jackets', 'Sweatshirts and Hoodies', 'Pants', 'Shorts', 'Tees']
shipping = 'For any exchanges or returns we offer a 30 day return policy on unopened and unworn products. Only regular priced items may be refunded, unfortunately sale items cannot be refunded.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
