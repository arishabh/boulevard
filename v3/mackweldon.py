from shopify import Shopify

NAME = 'mackweldon'
DISPLAY_NAME = 'Mack Weldon'
cats = ['boxer-briefs', 'trunks', 'briefs', 'boxers', 'long-underwear', 'high-socks', 'low-socks', 'tees', 'crew-neck-t-shirts', 'v-neck-t-shirts', 'long-sleeve', 'polos', 'button-ups', 'sweatshirts', 'pullovers', 'jackets-vests', 'pants', 'shorts', 'swim', 'large-bags', 'ion-travel-kit', 'wallets', 'hats', 'tech-cashmere-scarf', 'gloves']
shipping = 'Free shipping on orders over $50 and loyalty perks'
note = 'Final Upload'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
brand.post_collections()