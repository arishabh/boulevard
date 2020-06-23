from shopify import Shopify

WEB_NAME = 'bather' # Website name
DISPLAY_NAME = 'Bather - Apparel'
cats = ['swim', 'surf', 'all', 'patterned-swim-trunks', 'solid-swim-trunks', 'technical-surf-trunk', 'solid-surf-trunks', 'shirts', 'accessories', 'kids', 'sale', 'resort-2020']
cat_names = ['Swim Trunks | 5.5\"', 'Swim Trunks | 6.5\"']
imgs = ['https://drive.google.com/uc?export=download&id=1KEIejFNK9CUKITM2PeNFY9PVm-lGFOcr',
 'https://drive.google.com/uc?export=download&id=15PECtd8dO90jT30YQoTlN1goimhj_P_G',
 'https://drive.google.com/uc?export=download&id=14u9qe24IuKJ1AqwEc2J21Ui6I7w2CuH1']

shipping = 'Free shipping on orders over $100. All regular priced items are eligible for a return within fourteen days of the purchase date at the customers expense. Items must be unworn/unwashed with the original packaging and hangtags attached.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
