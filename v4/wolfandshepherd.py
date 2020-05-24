from shopify import Shopify

WEB_NAME = 'wolfandshepherd' # Website name
DISPLAY_NAME = 'Wolf & Shepherd' 
cats = ['dress-shoes', 'hybrids', 'drivers', 'sneakers', 'sale', 'accessories', 'lace-ups', 'slip-ons', 'monk-straps', 'sneakers', 'hybrids', 'boots', 'dress-socks', 'ws-belts']
cat_names = ['Dress Shoes', 'Hybrid Shoes', 'Drivers', 'Sneakers', 'Sale']
imgs = ['https://drive.google.com/uc?export=download&id=1PvbG--dpJmoeUkD_mXltfnlbzE5nOlKr',
 'https://drive.google.com/uc?export=download&id=1jVhLERVBOAVGsdUuXM3j5gB-mmexkRSA',
 'https://drive.google.com/uc?export=download&id=1AQT7b2lhyc8kn-O49t1Z8OyUA02CjxN6',
 'https://drive.google.com/uc?export=download&id=12hUDE5QBbpE-T-pUCvPhHPkeE_jSjxEm',
 'https://drive.google.com/uc?export=download&id=1xfU-kGrjDLBsULH_b5qrAczsZJLOjYeP',
 'https://drive.google.com/uc?export=download&id=1zQzUvNOROGzb0FxbZJ-ektz35dXcEi1J']

shipping = 'Returns are accepted on all full price, unworn, undamaged items within 30 days of purchase.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
