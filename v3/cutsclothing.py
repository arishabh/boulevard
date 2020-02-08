from shopify import Shopify

NAME = 'cutsclothing'  # e.g. onlyny | Has to be the same as on url (lowercase)
DISPLAY_NAME = 'Cuts'
cats = ['crew-neck', 'v-neck', 'henley', 'classic', 'split-hem', 'elongated', 'bestsellers', 'new-releases', 'fall-2019', 'long-sleeve']
note = 'Added display name for vendor and collection'
shipping = 'Free U.S. Shipping & Returns Over $100 | Free International Shipping Over $150'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()