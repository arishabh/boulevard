from shopify import Shopify

WEB_NAME = 'drinkhydrant' # Website name
DISPLAY_NAME = 'Hydrant'
cats = ['hydration-mix-P', 'rapid-hydration-mix-caffeine-P']
cat_names = ['Hydrant', 'Hydrant (w/ Caffeiene)']
imgs = []
shipping = 'Hydrant purchases come with free Standard Shipping, which is 3-5 Business Days. Expedited shipping is also available, which is 2-3 Business Days. Unfortunately, we don’t ship on Saturdays or Sundays. We offer a 30 day money back guarantee on our hydration mixes - if you are unhappy with your purchase for some reason, please let us know within 30 days at: hello@drinkhydrant.com'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
