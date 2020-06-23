from shopify import Shopify

NAME = 'vuoriclothing'
DISPLAY_NAME = 'Vuori - Apparel'
cats = ['new', 'best-sellers', 'bottoms', 'shorts', 'boardshorts', 'pants', 'short-sleeve-tops', 'long-sleeve-tops', 'hoodies-jackets', 'hats', 'travel', 'training', 'running', 'yoga']
cat_names = ['New', 'Best Sellers', 'Bottoms', 'Shorts', 'Boardshorts', 'Pants', 'Short Sleeve Tops', 'Long Sleeve Tops', 'Hoodies & Jackets']
shipping = 'Free ground shipping and returns over $75. Items must be unwashed and unworn'
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
