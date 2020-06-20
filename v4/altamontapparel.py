from shopify import Shopify

WEB_NAME = 'altamontapparel' # Website name
DISPLAY_NAME = 'Altamont - Apparel'
cats = ['new-arrivals', 't-shirts', 'knits-button-ups', 'denim', 'pants', 'sweatshirts', 'jackets', 'accessories']
cat_names = ['New Arrivals', 'Tees', 'Knits & Wovens', 'Denim', 'Pants', 'Hoodies & Sweaters', 'Jackets']
imgs = ['https://drive.google.com/uc?export=download&id=16rMzJ2svscyJSZukNctNWO4yVUAW7Z2P',
 'https://drive.google.com/uc?export=download&id=12sYkLFg85yBJ5TUMHZ6ryToVvlm7H_gy',
 'https://drive.google.com/uc?export=download&id=11yWAbDTFPKa8jyNVSliQ14BqZn2eY6QS',
 'https://drive.google.com/uc?export=download&id=1KGfeQx6komfw1oIaaBX2qMxoi-iGpN3N',
 'https://drive.google.com/uc?export=download&id=1XJHrI_Dexe54YMZaeYjCF2pwjwSeGJM_',
 'https://drive.google.com/uc?export=download&id=1uOcEU--0_B2jkcoQDybx52O9jPT5bBBj',
 'https://drive.google.com/uc?export=download&id=1D9sWtYDiZeDKs07WKc5Zg5h2oWvz91jA',
 'https://drive.google.com/uc?export=download&id=1kPrDoAvY_rLhEYX3QOzO0nhf7trczz6s']

shipping = 'Free shipping on U.S. orders over $100. You can return unworn and unused clothes to our warehouse within 30 days from point of purchase for a refund or store credit.'
note = 'New brand'

brand = Shopify(WEB_NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
# brand.post_collections(cat_names, imgs)
