from shopify import Shopify

WEB_NAME = 'beardbrand' # Website name
DISPLAY_NAME = 'Beard Brand - Grooming'
cats = ['beard', 'hair', 'body', 'kits', 'gear']
cat_names = ['Beard ', 'Hair', 'Body', 'Kits ', 'Gear']
imgs = ['https://drive.google.com/uc?export=download&id=1z85xCgu1G50uVGxrYfeRJqBWKFvh05yJ',
 'https://drive.google.com/uc?export=download&id=1Cuyf3iHwsl86A2fUtjhKnSbbvHNwGVym',
 'https://drive.google.com/uc?export=download&id=11yvSvR0z7_9quJwJ4OBXtUuHG2qlyL83',
 'https://drive.google.com/uc?export=download&id=1M_WeoAOLE-VgyaoK902nP8IazANYxkK-',
 'https://drive.google.com/uc?export=download&id=1vO8PKEHUDvFaNXE4AuiONqsb5zFNPZpj',
 'https://drive.google.com/uc?export=download&id=1ckLDWc_DioOUOx08RwIi4OE0sqTTZpBq']
shipping = 'Spend $50 more for free shipping! (USA Only) Free return available!'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
