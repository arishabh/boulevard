from shopify import Shopify

NAME = 'untuckit'  # e.g. onlyny | Has to be the same as on url (lowercase)
DISPLAY_NAME = 'Untuckit'
cats = ["shirts", "mens-new-arrivals", "wrinkle-free", "performance", "plaidsandflannels", "checksginghams", "prints", "solids-stripes", "short-sleeves", "tall", "relaxed-fit", "polos", "sweaters", "jackets-1", "tees-henleys", "bottoms", "shoes-accessories"]
cat_names = ['All Shirts', 'New Arrivals', 'Wrinkle Free', 'Performance', 'Plaids', 'Checks & Ginghams', 'Prints', 'Solids & Stripes', 'Short Sleeves', 'Tall Fit', 'Relaxed Fit', 'Polos', 'Sweaters', 'Jackets', 'T-Shirts and Henleys', 'Pants', 'Shoes and Accessories']
shipping = 'Free delivery for delivery in 5-7 business days. $8 for 2-4 days delivery. $20 for guarantee 2 days delivery. $25 for next business day delivery '
shipping += 'We accept returns of unworn, unwashed, undamaged or defective products within 30 days of the delivery date. '
note = 'Added display name for vendor and collection'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
brand.post_collections(cat_names)