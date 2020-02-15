from shopify import Shopify

NAME = 'johnnie-o' 
DISPLAY_NAME = 'Johnnie O'
cats = ['mens-sport-shirts', 'mens-polos', 'mens-pullovers-sweatshirts', 'mens-sweaters', 'jackets-vests', 'mens-t-shirts', 'mens-pants', 'mens-shorts', 'mens-swim', 'mens-hats-visors' ,'belts', 'shoes-socks', 'lifestyle']
cat_names = ['Sport Shirts', 'Polos', 'Pullovers & Sweatshirts', 'Sweaters', 'Jackets & Vests', 'T-Shirts', 'Pants', 'Shorts', 'Swim']
shipping = 'Free ground shipping over $85 & free returns'
note = 'Final Upload'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
brand.post_collections(cat_names)