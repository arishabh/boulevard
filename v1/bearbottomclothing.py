from general import *

NAME = 'bearbottomclothing'
start = time()
tot = 0
url = ['https://bearbottomclothing.com/collections/',  '/products.json?limit=250&page=']
cats=['7-run-shorts', '5-5-rec-shorts', '7-rec-shorts', '5-5-run-shorts', '7-drifter-shorts', 'swim', 'tech-tee', 'core-tee', 'outerwear', 'paracord-bracelets', 'gear']
check_tags=['stretch-shorts', 'stretch-jogger', 'stretch-swim', 'hybrid-shorts', 'drifter-shorts', 'bracelet', 'tees', 'gear', 'drawstrings-shorts', 'briefs', 'fleece', 'shorts', 'shirt', 'collar', 'active-shorts', 'casual-shorts', 'pants']
i=2
file_name = NAME.title()+'Inventory.csv'
rows = headers
g_total = 0
prods = []

for c in cats:
    b = bs(get(url[0]+c+url[1]+'1').content, 'html.parser').getText()
    data = json.loads(b)['products']
    g_total += len(data)
    while(data != []):
        for d in data:
            if(check(d)): continue
            prod = Shopify()
            prod.tags = [gen_clean(d['vendor'])]
            all_tags = gen_clean_li(d['tags'])
            if(all_tags == []): continue
            for a in cats:
                if(a in all_tags and a not in prod.tags):
                    prod.tags.append(a)
            for a in check_tags:
                if(a in all_tags and a not in prod.tags):
                    prod.tags.append(a)

            others(url, prod, d, c, NAME)

            details = clean_text(d['body_html'])
            size = 'Click buy for more sizing information.'
            shipping = 'We offer FREE standard shipping in the US on all orders $99+. $5 standard shipping on all other orders. Most orders ship out the next business day. Some even go out the same day.'
            shipping += 'We offer free exchanges within 30 days of placing your order for unworn and unwashed products. We can not accept any international returns or exchanges.'
            prod.body = make_body(details, size, shipping)

            if(prod in prods): continue
            tot += 1
            prods.append(prod)
            rows += prod.get_rows()
        i += 1
        data = json.loads(bs(get(url[0]+c+url[1]+str(i)).content, 'html.parser').getText())['products']
        g_total += len(data)
write_csv(file_name, rows)
print("Total products: " + str(tot) + "/" + str(g_total) + "\nTotal Time: " + str(round(time()-start, 2)) + 's')
