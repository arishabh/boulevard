from general import *

start = time()
tot = 0
url = ['https://www.onlyny.com/collections/', '/products.json?limit=250&page=']
cats = ['new-arrivals', 'tees', 'tops', 'bottoms', 'outerwear', 'sweatshirts', 'swim-shorts', 'accessories']
check_tags = ['bags', 'mugs', 'hats', 'knit hats', 't-shirts']
i=2
file_name = 'OnlyNYInventory.csv'
rows = headers
g_total = 0
prods = []

for c in cats:
    b = bs(get(url[0]+c+url[1]+'1').content, 'html.parser').getText()
    data = json.loads(b)['products']
    g_total += len(data)
    while(data != []):
        for d in data:
            prod = Shopify()
            prod.tags = [d['vendor'].lower().replace(' ', '-'), c]
            all_tags = list(map(str.lower, d['tags']))
            for a in cats:
                if(a in all_tags and a not in prod.tags):
                    prod.tags.append(a.replace(' ', '-'))
            for a in check_tags:
                if(a in all_tags and a not in prod.tags):
                    prod.tags.append(a)
            prod.vendor = 'OnlyNY-men'
            prod.collection = 'OnlyNY-men'
            prod.title = d['title']
            prod.handle = d['handle']
            prod.type = d['product_type'].lower()

            var = d['variants'][0]
            prod.price = var['price']
            prod.weight = var['grams']
            prod.tax = var['taxable']
            prod.ship = var['requires_shipping']
            prod.sku = var['sku']
            prod.cap = var['compare_at_price']
            prod.link = url[0]+c+'/products/'+'-'.join(prod.title.lower().split())

            prod.img_urls = [img['src'] for img in d['images']]
            prod.img_pos = [img['position'] for img in d['images']]

            raw = clean_text(d['body_html'])
            details = ' '.join(clean_text(d['body_html']).split('***')[:-1])
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
