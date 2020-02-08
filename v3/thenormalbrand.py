from shopify import Shopify

NAME = 'thenormalbrand'
DISPLAY_NAME = 'The Normal Brand'
cats = ['outerwear', 'hats', 'accessories', 'sweaters-pullovers', 'button-up-shirts', 't-shirts', 'henleys', 'pants', 'new', 'bestseller', 'shirts']
shipping = 'Returns and exchanges for unwashed and unworn items in original condition will be accepted up to 30 days from the date of purchase.'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()