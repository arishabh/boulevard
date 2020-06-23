from shopify import Shopify

WEB_NAME = 'supply'  # Website name
DISPLAY_NAME = 'Supply - Grooming'
cats = ['the-single-edge-razor-P', 'grooming-essentials', 'skincare', 'accessories', 'the-single-edge-starter-set', 'fathers-day-shaving-gift-set']
cat_names = ['Razors', 'Grooming essentials', 'Skin Essentials', 'Blades and accesories']
imgs = ['https://drive.google.com/uc?export=download&id=1H8UNVhHSD1Mad3EvREQiBd9b-1F_BsxE',
 'https://drive.google.com/uc?export=download&id=1MZ_ygkDygd_HzLLPCDU2pft0xR-BdEmL',
 'https://drive.google.com/uc?export=download&id=1l_j16J51RIelM_t9ugj7Jz0bFmnF9LbW',
 'https://drive.google.com/uc?export=download&id=1cnwoAuFrp_9BK_ekdGLcXf1yiwjO_SOm',
 'https://drive.google.com/uc?export=download&id=1J8qPRujU0GGqR2lEyRnKCtYU3650MCym',
 'https://drive.google.com/uc?export=download&id=1E1izkSViYr8km5kVuOSCFvnDapw3Uchn']
shipping = 'Free US shipping on any order of $35 or more. We offer a 60 Day Trial for all of our gear, which means you have 60 days to try it out, live with it, and love it. If at any point in the first 60 days you decide that you are not 100% satisfied with your new products, return them for a full refund—no questions asked. Our return policy is simple - love our products, or send them back.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.url[0] = 'https://www.supply.co/collections/'
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
