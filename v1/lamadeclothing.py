from general import *

start = time()
tot = 0
url = ['https://lamadeclothing.com/collections/', '/products.json?limit=250&page=']
cats = {'mens':'new-arrivals', 'mens-tees':'tees'}
i=2
file_name = 'LAmadeInventory.csv'
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
            prod.tags = [d['vendor'].lower().replace(' ', '-'), 'tees', 'new-arrivals']
            others(url, prod, d, c, 'LAmadecothing')

            details = clean_text(d['body_html'])
            size = 'Click buy for more sizing information.'
            shipping = 'We currently offer USPS or UPS Ground shipping at a flat rate of $8 for orders within the continental US.'
            shipping += 'We do offer expedited shipping options. 2nd Day and Next Day Air for $19.00 and $40.00.'
            shipping += 'Orders over $100 will require a signature confirmation upon delivery.'
            shipping += 'If you are not completely satisfied with your purchase, you may return it back to LA Made within 14 days of your purchase for a full return.'
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
