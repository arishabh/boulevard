from general import *

start = time()
tot = 0
url = ['https://clearweatherbrand.com/collections/', '/products.json?limit=250&page=']
cats = ['new-arrivals-2', 'mens', 'black-friday-1', 'clearweather-compadres']
check_tags = ['mens', 'new arrivals', 'footwear', 'boots', 'apparel', 'sneakers', 'sweatshirts']
i=2
file_name = 'ClearWeatherBrandInventory.csv'
rows = headers
g_total = 0
prods = []

for c in cats:
    b = bs(get(url[0]+c+url[1]+'1').content, 'html.parser').getText()
    data = json.loads(b)['products']
    g_total += len(data)
    while(data != []):
        for d in data:
            if (not any([v['available'] for v in d['variants']])): continue
            prod = Shopify()
            prod.tags = [d['vendor'].lower().replace(' ', '-'), c]
            all_tags = list(map(str.lower, d['tags']))
            for a in check_tags:
                if(a in all_tags and a not in prod.tags):
                    if(a == 'mens'):
                        prod.tags.append(a)
                        prod.tags.append('shoes')
                    else: prod.tags.append(a.replace(' ', '-'))

            others(url, prod, d, c, 'Clearweatherbrand')

            details = clean_text(d['body_html'])
            size = 'Click buy for more sizing information.'
            shipping = 'Most Orders Are Processed And Shipped Within 1-2 Business Days Of Purchase However Please Allow Up To 5 Business Days For Processing All Orders Are Shipped From New York City And Delivery Time Is Based On Shipping Method.'
            shipping += 'Full priced items purchased from onlyny.com are eligible for a full refund or exchange if returned within 30 days of purchase. Any already marked down items are not eligible for return, but can be exchanged for anything else on the website.'
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
