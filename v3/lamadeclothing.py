from shopify import Shopify

NAME = 'lamadeclothing'
DISPLAY_NAME = 'LAmade'
cats = ['mens', 'mens-tees']
note = 'Added display name for vendor and collection'
shipping = 'We currently offer USPS or UPS Ground shipping at a flat rate of $8 for orders within the continental US.'
shipping += 'We do offer expedited shipping options. 2nd Day and Next Day Air for $19.00 and $40.00.'
shipping += 'Orders over $100 will require a signature confirmation upon delivery.'
shipping += 'If you are not completely satisfied with your purchase, you may return it back to LA Made within 14 days of your purchase for a full return.'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections()