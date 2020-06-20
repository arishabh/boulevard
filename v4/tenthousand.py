from shopify import Shopify

NAME = 'tenthousand'
DISPLAY_NAME = 'Ten Thousand - Apparel'
cats = ['']
shipping = 'Free shipping. Free returns'
note = 'Changed the URl (with https)'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.url = ['https://www.' + NAME + '.cc', '/products.json?limit=250&page=']
brand.link = brand.url[0]+'/'
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()
