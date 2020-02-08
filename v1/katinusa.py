from general import *

start = time()
tot = 0
url = ['https://www.katinusa.com/collections/', '/products.json?limit=250&page=']
cats = ['tops', 'bottoms', 'trunks-1', 'knits', 'flannel', 'shirts', 'sweaters', 'jackets-1', 'shorts', 'pants', 'new-arrivals', 'accessories']
check_tags = ['jackets', 'fleece', 'shirt', 'tees', 'graphic-tees', 'towel', 'hats', 'beanies', 'keychain', 'pins']
i=2
file_name = 'KatinUSAInventory.csv'
rows = headers
g_total = 0
prods = []

for c in cats:
    b = bs(get(url[0]+c+url[1]+'1').content, 'html.parser').getText()
    data = json.loads(b)['products']
    g_total += len(data)
    while(data != []):
        for d in data:
            if('gift' in d['title'].lower() or 'gift' in d['handle'].lower() or 'gift' in d['product_type']): continue
            if (not any([v['available'] for v in d['variants']])): continue
            prod = Shopify()
            prod.tags = [d['vendor'].lower().replace(' ', '-'), c.split('-1')[0]]
            all_tags = list(map(lambda x: x.lower().replace(' ', '-'), d['tags']))
            for a in cats:
                a = a.split('-1')[0]
                if(a in all_tags and a not in prod.tags):
                    prod.tags.append(a)
            for a in check_tags:
                if(a in all_tags and a not in prod.tags):
                    prod.tags.append(a)

            others(url, prod, d, c, 'katinusa')

            details = clean_text(d['body_html'])
            size = 'Click buy for more sizing information.'
            shipping = 'For up to 30 days, we’ll gladly accept unworn, unwashed, or defective merchandise purchased on katinusa.com for return or exchange.'
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
