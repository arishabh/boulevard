from shopify import Shopify

NAME = 'cutsclothing'
DISPLAY_NAME = 'Cuts'
cats = ['crew-neck', 'v-neck', 'henley', 'classic', 'split-hem', 'elongated', 'bestsellers', 'new-releases', 'fall-2019', 'long-sleeve']
cat_names = ['Crew Neck', 'V-Neck', 'Henley', 'Classic Cut', 'Split Hem', 'Elongated']
shipping = 'Free U.S. Shipping & Returns Over $100 | Free International Shipping Over $150'
note = 'Final Upload'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.url = ['https://shop.' + NAME + '.com/collections/', '/products.json?limit=250&page=']
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
