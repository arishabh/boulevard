from shopify import Shopify

NAME = 'barneycools'  # e.g. onlyny | Has to be the same as on url (lowercase)
DISPLAY_NAME = 'Barney Cools'
cats = ['tees-tanks', 'woven-shirts', 'fleece-and-knits', 'jackets', 'shorts', 'pants', 'accessories', 'footwear', 'poolside-suits', 'hats', 'socks-1', 'socks', 'underwear', 'online-exclusive']
shipping = 'Premium DHL Express shipping is free on all orders over $100, and $25 for small orders less than $100.'
shipping += 'Returns are only available on sale items if they are faulty or damaged.'
note = 'Has sizes in the Title option'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
brand.post_collections()