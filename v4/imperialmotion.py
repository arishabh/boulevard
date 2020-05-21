from shopify import Shopify

WEB_NAME = 'imperialmotion' # Website name
DISPLAY_NAME = 'Imperial Motion' 
cats = ['mens-tees-and-tanks', 'knits', 'shirts', 'sweatshirts', 'mens-jackets', 'tub-shorts',  'mens-boardshorts', 'mens-pants', 'mens-shorts', 'mens-bottoms', 'liberty-chino-pant-faded-black', 'boxer-briefs',  'mens-wetsuits', 'mens-wetsuits', 'wetsuit-accessories', 'lux-wetsuit', 'accessories', 'backpacks-and-bags', 'hats', 'beanies', 'socks', 'boxer-briefs', 'always-evolving', 'always-evolving', 'control-freak', 'ghost-reflective', 'reflective', 'nano-cure-tech', 'mens-tops']
cat_names = ['Tees & Tanks', 'Knits', 'Shirts', 'Sweatshirts/Fleece', 'Jackets', 'Seeker Volley Shorts', 'Boardshorts', 'Pants', 'Shorts']
shipping = 'Free shipping on orders over $50. Free returns and exchanges for unused and unworn clothes within 30 days.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
