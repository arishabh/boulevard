from shopify import Shopify

NAME = 'publicrec'  # e.g. onlyny | Has to be the same as on url (lowercase)
DISPLAY_NAME = 'Public Rec'
cats = ['bottoms-pants', 'bottoms-shorts', 'tops-t-shirts', 'tops-henleys', 'tops-polos', 'politan-hoodie', 'layers-jackets', 'pro-back-both-sizes', 'pro-weekender', 'pro-travel-kit', 'baseball', 'chill-beanie']
shipping = 'Free shipping, free returns, free exchnages'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()