from shopify import Shopify

NAME = 'thecriticalslidesociety'
DISPLAY_NAME = 'Critical Slide'
cats = ['tshirts', 'boardshorts', 'walkshorts', 'shirts', 'pants', 'jackets', 'knits', 'sweats-fleece', 'hats-caps', 'wetsuits', 'accessories', 'shoes-socks']
shipping = 'Free shipping and returns in Australia.'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()