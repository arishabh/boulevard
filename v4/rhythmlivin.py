from shopify import Shopify

WEB_NAME = 'rhythmlivin' # Website name
DISPLAY_NAME = 'Rhythm' 
cats = ['mens-new-arrivals', 'mens-top-sellers', 'mens-t-shirts', 'mens-shorts', 'mens-trunks', 'mens-woven-shirts', 'mens-knits', 'mens-bottoms', 'mens-jackets', 'vintage-tees', 'mens-linen',  'mens-fleece', 'boys-clothing', 'mens-sale', 'mens-accessories', 'mens-bags', 'mens-headwear', 'mens-sunglasses', 'mens-wallets', 'mens-sale-accessories', 'surf-lifestyle', 'beach-essentials', 'rhythm-x-klean-kanteen', 'mens-grooming', 'surfboards', 'suncare', 'surf-goods', 'rhythm-wetsuits', 'mens-jan20-collection']
cat_names = ['New Arrivals', 'Top Sellers', 'T-Shirts', 'Shorts', 'Trunks', 'Woven Shirts', 'Knits', 'Pants', 'Jackets']
imgs = ['https://drive.google.com/uc?export=download&id=17byA-Q2JaixUHYoP6UFdkFFgJn6QwiRR',
 'https://drive.google.com/uc?export=download&id=1OoLjnhPe8_2c_Bj8P5A4z9onsX4mbBgg',
 'https://drive.google.com/uc?export=download&id=1ACVVuaZ4x0WBZmPbz-cgCPEO8GYN4YBa',
 'https://drive.google.com/uc?export=download&id=1ZnxaojFkaNK-Z967Enlj2ug6nZ4W2_sW',
 'https://drive.google.com/uc?export=download&id=1hYlv24mFqH-az1nqCthm-uYOvSLV_hp2',
 'https://drive.google.com/uc?export=download&id=1UHaOmtKwchQlmxPYerZUg20nXuuLAwwF',
 'https://drive.google.com/uc?export=download&id=1Nmdkkg0hgKtdTZTX1MamrlTm5AHVzJJF',
 'https://drive.google.com/uc?export=download&id=1Hd28QUSmISh_wOuIX7R5WjveLveHYyYP',
 'https://drive.google.com/uc?export=download&id=1bnWKLWJ4cPGreRWTsAgrmLlpz8A1LdxI',
 'https://drive.google.com/uc?export=download&id=12_VhSDF_1oTDO4jZk1BiYorj9kA-e5o9']

shipping = 'Free express shipping on orders above $75. If you’re not happy with your purchase we are happy to now offer refunds on all full-priced purchases and store credits on sale styles, subject to some limited exclusions.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
