from shopify import Shopify

WEB_NAME = 'blackwolfnation' # Website name
DISPLAY_NAME = 'Black Wolf - Grooming'
cats = ['individual-products', 'bundles-1', 'gear', 'shower-bundle-P', 'blackout-bundle-for-oily-skin-P', 'body-face-wash-bundle-P', 'activated-charcoal-bundle-P', 'complete-skincare-bundle-new-1-P']
cat_names = ['Products', 'Solutions', 'Merch']
imgs = ['https://drive.google.com/uc?export=download&id=1COsMelsdroZDxHmkh0nKuXH4czxy7zEH',
        'https://drive.google.com/uc?export=download&id=136vTaALN4_nm43vonoShYIbBUIZKSmX0',
        'https://drive.google.com/uc?export=download&id=1mZmZGKh0fOz7uo8YrfvQxAPJr_jn7tuh',
        'https://drive.google.com/uc?export=download&id=1eb7qzb5hBKHsMtLyCDbxGAKnRKZvO8PA']
shipping = 'If you are not satisfied, you may return the products within 30 days of delivery. We do not provide shipping labels. Within the USA, Puerto Rico and Canada, standard shipping is always FREE on orders over $30! Otherwise we have a small flat fee of $3.99 for orders under $30.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
