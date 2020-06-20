from shopify import Shopify

NAME = 'publicrec'  # e.g. onlyny | Has to be the same as on url (lowercase)
DISPLAY_NAME = 'Public Rec - Apparel'
cats = ['bottoms-pants', 'bottoms-shorts', 'tops-t-shirts', 'tops-henleys', 'tops-polos', 'layers-jackets']
cat_names = ['Pants', 'Shorts', 'T-Shirts', 'Henleys', 'Polos', 'Jackets']
shipping = 'Free shipping, free returns, free exchnages'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
