from shopify import Shopify

WEB_NAME = 'bather' # Website name
DISPLAY_NAME = 'Bather' 
cats = ['swim', 'surf', 'all', 'patterned-swim-trunks', 'solid-swim-trunks', 'technical-surf-trunk', 'solid-surf-trunks', 'shirts', 'accessories', 'kids', 'sale', 'resort-2020']
cat_names = ['Swim Trunks | 5.5\"', 'Swim Trunks | 6.5\"', 'More']
shipping = 'Free shipping on orders over $100. All regular priced items are eligible for a return within fourteen days of the purchase date at the customers expense. Items must be unworn/unwashed with the original packaging and hangtags attached.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names)
