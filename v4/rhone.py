from shopify import Shopify

WEB_NAME = 'rhone' # Website name
DISPLAY_NAME = 'Rhone' 
cats = ['workout-shirts-for-men', 'mens-short-sleeve-workout-shirts', 'mens-long-sleeve-shirts', 'mens-workout-tank-tops', 'button-downs', 'mens-polo-shirts', 'henley-collection', 'hoodies-pullovers', 'coats-jackets', 'vests', 'mens-athletic-pants-and-shorts', 'casual-shorts', 'mens-workout-shorts', 'mens-workout-pants', 'joggers', 'sweatpants-lounge', 'training-pants', 'tights', 'mens-board-shorts', 'workout-accessories-for-men', 'boxers', 'running-socks-for-men', 'mens-outdoor-hats']
cat_names = ['Tops', 'Short Sleeve', 'Long Sleeve', 'Tanks', 'Button Downs', 'Polos', 'Henleys', 'Hoodies & Pullovers', 'Coats & Jackets', 'Vests', 'Bottoms', 'Casual Shorts', 'Athletic Shorts', 'Pants', 'Joggers', 'Sweatpants & Lounge', 'Training Pants', 'Tights', 'Swim', 'Accessories', 'Boxers', 'Socks', 'Caps']
shipping = 'Rhone garments in their original, unworn, and unwashed condition may be exchanged or returned for a refund up to 45 days following the original date of purchase free of charge and with free shipping. Shipping is free for delivery in 5-7 business days. Faster shipping options are available but chargable'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
