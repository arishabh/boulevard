from shopify import Shopify

NAME = 'taylrdclothing'
DISPLAY_NAME = 'Taylrd'
cats = ['new-tops', 'new-bottoms', 'all-chinos', '5-pockets', 'shorts', 'joggers', 'long-sleeve-button-downs', 'short-sleeve', 'hoodies-and-jackets', 'hoodies', 'henleys-and-tees', 'brushed-button-downs']
shipping = 'Free standard shipping and return over $75. Free Express shipping over $150'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()