from shopify import Shopify

NAME = 'onlyny'
DISPLAY_NAME = 'OnlyNY'
cats = ['new-arrivals', 'tees', 'tops', 'bottoms', 'outerwear', 'sweatshirts', 'swim-shorts', 'accessories']
note = 'Added display name for vendor and collection'
shipping = 'Most Orders Are Processed And Shipped Within 1-2 Business Days Of Purchase However Please Allow Up To 5 Business Days For Processing All Orders Are Shipped From New York City And Delivery Time Is Based On Shipping Method.'
shipping += 'Full priced items purchased from onlyny.com are eligible for a full refund or exchange if returned within 30 days of purchase. Any already marked down items are not eligible for return, but can be exchanged for anything else on the website.'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()