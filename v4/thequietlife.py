from shopify import Shopify

WEB_NAME = 'thequietlife' # Website name
DISPLAY_NAME = 'Quiet Life' 
cats = ['new-arrivals', 't-shirts', 'cut-sew', 'fleece', 'hats', 'capsules', 'accessories', 'sale-section', 'make-new-friends', 'splatter', 'neon-tye-dye', 'camera-strap-collectino', '2020-spring-d1', '2019-fall-drop-2', '2019-fall-drop-1', 'bottoms', 'jackets-coats', 'shirts', 'crew-sweats', 'pullover-hoods', 'long-sleeve-ts', 'graphic-ts', 'custom-ts', 'polo-hats', '5-panel-hats', 'snapback-hats', 'bucket-hats', 'dad-hats', 'beanie-hats', 'sale-cut-sew-1', 'sale-fleece', 'sale-t-shirts', 'sale-hats-1', 'sale-accessory']
cat_names = ['New Arrivals', 'T-Shirts', 'Cut & Sew', 'Fleece', 'Hats', 'Sale', 'Accessories']
shipping = 'Standard delivery is 3-7 working days, depending on the service you choose. Customs of each country may delay this time. The shipping cost will depend on size and weight of your package. With USPS, once your parcel has arrived in your country, it will be passed on to an internal postal service, according to standard delivery procedures. A signature is required upon delivery.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.url = ['https://shop.' + WEB_NAME + '.com/collections/', '/products.json?limit=250&page=']
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
