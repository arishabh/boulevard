from shopify import Shopify

WEB_NAME = 'artofsport' # Website name
DISPLAY_NAME = 'Art of Sport - Grooming'
cats = ['shower', 'deodorants', 'skin', 'all']
cat_names = ['Shower', 'Deodorant', 'Face + Body']
imgs = ['https://drive.google.com/uc?export=download&id=1t-mtjO_wSkOPoQe2TNc4t-QzkD7zkPAl',
 'https://drive.google.com/uc?export=download&id=1IPUj53ay5yrb9OUbyKuNOXNexBrmyuup',
 'https://drive.google.com/uc?export=download&id=17f8I5TTreQJqSG0MpdaNZ5UcMRgi40By',
 'https://drive.google.com/uc?export=download&id=1vye-YPYs3p7TOYtJW9RhuWXAwBce8g7a']
shipping = 'If you would like to exchange or return a product, please contact AOS Support within 365 days of the purchase. Free shipping with orders $30+'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
