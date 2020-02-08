from shopify import Shopify

NAME = 'corridornyc' #e.g. onlyny | Has to be the same as on url
DISPLAY_NAME = 'Corridor'
cats=['shirts', 'outerwear', 'sweaters', 't-shirt', 'bottoms', 'suits', 'accessories-1', 'new-arrivals-1', 'friends-of-friends', 'things-theyll-need', 'city-rustic', 'clean-and-classy', 'modern-minimalist']
note = 'Added display name for vendor and collection'
shipping = 'We accept returns and exchanges within 14 days of the product delivery date. Items must not be worn, washed or damaged, and must have applicable '
shipping += 'tags attached in order to be eligible for a return or exchange. Items marked as final sale are not eligible for returns or exchanges. '
shipping += 'Domestic returns and exchanges are free for orders over $250.'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()