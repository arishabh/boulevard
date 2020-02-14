from shopify import Shopify

NAME = 'johnnie-o' 
DISPLAY_NAME = 'Johnnie O'
cats = ['mens-polos', 'mens-sport-shirts', 'mens-pullovers-sweatshirts', 'mens-sweaters', 'jackets-vests', 'mens-t-shirts', 'mens-pants', 'mens-shorts', 'mens-swim', 'mens-hats-visors' ,'belts', 'shoes-socks', 'lifestyle']
shipping = 'FREE GROUND SHIPPING ON ORDERS OVER $85 & FREE RETURNS'.lower()
note = 'Final Upload'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
brand.post_collections()