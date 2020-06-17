from shopify import Shopify

WEB_NAME = 'jackhenry' # Website name
DISPLAY_NAME = 'Jack Henry' 
cats = ['hair', 'face', 'body', 'kits']
cat_names = ['Hair', 'Face', 'Body', 'Kits']
imgs = ['https://drive.google.com/open?id=1FZrsL4sB-l5QlYDZktnJuP1i8_qxJqQm',
 'https://drive.google.com/open?id=1a2ixh4okYCukZfRK6Usfnlqu1cqVGkYt',
 'https://drive.google.com/open?id=1b3qqq8o5AUmCNlwqIQtsIjwJtZo2vDqA',
 'https://drive.google.com/open?id=1ysaoLFmDrGP4BGKY3UVYipdfw63HTfQx',
 'https://drive.google.com/open?id=1wCb0QgPrCwqcsIPyAplmZJgg94J_dIO5']
shipping = 'Free shipping and free returns. Returns available for unworn and unused products.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.url[0] = 'https://jackhenry.co/collections/'
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
