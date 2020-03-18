from shopify import Shopify

NAME = 'taylrdclothing'
DISPLAY_NAME = 'Taylrd'
cats = ['new-arrivals', 'bottoms', 'tops', 'long-sleeve-button-downs', 'short-sleeve', 'henleys-and-tees', 'hoodies-and-jackets', 'all-chinos', 'joggers', 'shorts', '5-pockets', 'final-sale', 'brushed-button-downs']
cat_names = ['New Arrivals', 'Bottoms ', 'Tops', 'L/S Button Downs', 'S/S Buttondowns', 'Henleys & Tees', 'Hoodies & Jackets', 'Chinos', 'Joggers', 'Shorts', '5 Pocket Pants', 'Final Sale']
shipping = 'Free standard shipping and return over $75. Free Express shipping over $150'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
