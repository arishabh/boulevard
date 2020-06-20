from shopify import Shopify

NAME = 'mackweldon'
DISPLAY_NAME = 'Mack Weldon - Apparel'
cats = ['bestsellers', 'underwear', 'socks', 'tops', 'bottoms', 'accessories']
cat_names = ['Bestsellers', 'Underwear', 'Socks', 'Tops', 'Bottoms', 'Accessories']
shipping = 'Free shipping on orders over $50 and loyalty perks'
note = 'Final Upload'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
