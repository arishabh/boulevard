from shopify import Shopify

WEB_NAME = 'imperialmotion' # Website name
DISPLAY_NAME = 'Imperial Motion' 
cats = ['tub-shorts', 'mens-boardshorts', 'mens-shorts', 'mens-pants', 'mens-tees-and-tanks', 'knits', 'shirts', 'sweatshirts', 'mens-jackets', 'mens-bottoms', 'liberty-chino-pant-faded-black', 'boxer-briefs',  'mens-wetsuits', 'mens-wetsuits', 'wetsuit-accessories', 'lux-wetsuit', 'accessories', 'backpacks-and-bags', 'hats', 'beanies', 'socks', 'boxer-briefs', 'always-evolving', 'always-evolving', 'control-freak', 'ghost-reflective', 'reflective', 'nano-cure-tech', 'mens-tops']
cat_names = ['Seeker Volley Shorts', 'Boardshorts', 'Shorts', 'Pants', 'Tees & Tanks', 'Knits', 'Shirts', 'Sweatshirts/Fleece', 'Jackets']
imgs = ['https://drive.google.com/uc?export=download&id=1Wu2N-PMkvHBBjoWw1w4-RIKSvhLAvL6D',
 'https://drive.google.com/uc?export=download&id=1btsjsHrxropZCWSfnT5UOJUODY8PFjcb',
 'https://drive.google.com/uc?export=download&id=1Hynkpfr3iLV_hqY5ERNaNIXv-zMhuNVO',
 'https://drive.google.com/uc?export=download&id=1yX6jLc23Dkj7dQ0iTF0OHOvO9xGdH41U',
 'https://drive.google.com/uc?export=download&id=1XPSDY58b1JOJQt-WVawceci478heV1Rw',
 'https://drive.google.com/uc?export=download&id=1DwdmBuZDyV_60DWwPr1xtEgL_7fa6q1q',
 'https://drive.google.com/uc?export=download&id=1P1B6KiUUgw79NK2J1W1OO0TTHJkiJwmN',
 'https://drive.google.com/uc?export=download&id=16hrlmOq7K0b7twEYBNBsSOwKX4UPV3XR',
 'https://drive.google.com/uc?export=download&id=17rTdYBDh_0BsqENXXHVJ5PFHuP09rFuA',
 'https://drive.google.com/uc?export=download&id=1_YenKNaAKZNbDVmBemQFU7Z-wVIFcY8L']


shipping = 'Free shipping on orders over $50. Free returns and exchanges for unused and unworn clothes within 30 days.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
