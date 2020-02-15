from shopify import Shopify

NAME = 'tenthousand'
DISPLAY_NAME = 'Ten Thousand'
cats = ['']
shipping = 'Free shipping. Free returns'
note = 'Changed the URl (with https)'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.url = ['https://www.' + NAME + '.cc', '/products.json?limit=250&page=']
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()