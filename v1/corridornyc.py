from general import *

NAME = 'corridornyc'
start = time()
tot = 0
url = ['https://corridornyc.com/collections/',  '/products.json?limit=250&page=']
cats=['shirts', 'outerwear', 'sweaters', 't-shirt', 'bottoms', 'suits', 'accessories-1', 'new-arrivals-1', 'friends-of-friends', 'things-theyll-want', 'things-theyll-need', 'city-rustic', 'clean-and-classy', 'modern-minimalist']
check_tags=['cableami', 'hoodie', 'sweater', 'pants', 'scarf', 'suiting', 'hats', 'crewneck-sweater', 'studebaker', 'craighill']
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
            if(gift_ava(d)): continue
            prod = Shopify()
            prod.tags = [gen_clean(d['vendor']), gen_clean(c)]
            all_tags = gen_clean_li(d['tags'])
            if(all_tags == []): continue
            for a in cats:
                a=gen_clean(a)
                if(a in all_tags and a not in prod.tags):
                    prod.tags.append(a)
            for a in check_tags:
                if(a in all_tags and a not in prod.tags):
                    prod.tags.append(a)

            others(url, prod, d, c, NAME)
            prod.link='https://corridornyc.com/products/'+d['handle']

            details = clean_text(d['body_html'])
            size = 'Click buy for more sizing information.'
            shipping = 'We typically dispatch orders within 2 business days from the date that we receive your order and credit verification has been confirmed. International orders may take up to 3-5 business days to process.'
            shipping += 'We accept returns and exchanges for unworn, unwashed and undamaged products within 14 days of the product delivery date.'
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
