from shopify import Shopify

NAME = 'clearweatherbrand'  
DISPLAY_NAME = 'Clearweather'
cats = ['new-arrivals-2', 'mens/footwear', 'clear-weather-skateboarding', 'black-friday-1', 'clearweather-compadres/apparel']
shipping = 'Most Orders Are Processed And Shipped Within 1-2 Business Days Of Purchase However Please Allow Up To 5 Business Days For Processing All Orders Are Shipped From New York City And Delivery Time Is Based On Shipping Method.'
shipping += 'Full priced items purchased from onlyny.com are eligible for a full refund or exchange if returned within 30 days of purchase. Any already marked down items are not eligible for return, but can be exchanged for anything else on the website.'
note = 'Final upload'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()