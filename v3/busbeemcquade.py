from general import *

NAME = 'busbeemcquade'  # e.g. onlyny | Has to be the same as on url (lowercase)
DISPLAY_NAME = 'Busbee McQuade'
cats = ['men']
shipping = 'We are proud to offer FREE 3 Day Shipping for all orders over $99. Orders under this amount still enjoy 2 Day Shipping but are charged a flat rate of $5. Next day shipping are charged a flat rate of $20'
shipping += 'We accept returns within 30 days of your purchase for a full refund. All return items must be unworn, unwashed and undamaged with original tags still intact and in the original poly bags.'            prod.body = make_body(details, size, shipping)

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()