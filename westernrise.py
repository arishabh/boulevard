from shopify import Shopify

NAME = 'westernrise'
DISPLAY_NAME = 'Western Rise - Apparel'
cats = ['best-sellers', 'new-arrivals', 'mens-shirts', 'mens-bottoms', 'outerwear', 'merino-wool', 'accessories']
cat_names = ['Best Sellers', 'New Arrivals', 'Tops', 'Bottoms', 'Outerwear', 'Merino Wool', 'Accessories']
shipping = 'Free shipping and return available for orders above $150. Returns will be eligible for full refund within 60 days of purchase'
note = 'Repeats so many products' 

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
