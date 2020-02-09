from shopify import Shopify

NAME = 'bearbottomclothing'
DISPLAY_NAME = 'Bearbottom'
cats=['7-run-shorts', '5-5-rec-shorts', '7-rec-shorts', '5-5-run-shorts', '7-drifter-shorts', '5-5-stretch-shorts', '7-stretch-shorts', '7-easy-shorts', '8-hybrid-shorts', '8-sateen-shorts', '7-drawstring-shorts', 'swim', 'tech-tee', 'core-tee', 'outerwear', 'paracord-bracelets', 'gear']
shipping = 'We offer FREE standard shipping in the US on all orders $99+. $5 standard shipping on all other orders. Most orders ship out the next business day. Some even go out the same day.'
shipping += 'We offer free exchanges within 30 days of placing your order for unworn and unwashed products. We can not accept any international returns or exchanges.'
note = 'Final upload'

brand = Shopify(NAME, DISPLAY_NAME, cats, shipping, note)
brand.run()
brand.write_csv()
brand.write_info()
brand.post_collections()