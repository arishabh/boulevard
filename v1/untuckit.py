from general import *

start = time()
tot = 0
url = 'https://www.untuckit.com/products.json?limit=250&page='
i=2
b = bs(get(url+'1').content, 'html.parser').getText()
data = json.loads(b)['products']
file_name = 'UntuckeditInventory.csv'
rows = headers
g_total = len(data)

while(data != []):
    for d in data:
        prod = Shopify()
        all_tags = list_new(d['tags'])
        prod.tags = [d['vendor']]
        try:
            if(all_tags['department'] != 'men'): continue
        except:
            pass
        if(not d['variants'][0]['available']): continue

        sleeve = all_tags.get('sleeve-length', '')
        fabric = all_tags.get('fabric', '')
        subcat = all_tags.get('subcat', '')
        cat = all_tags.get('catagory', '')
        if('wrinkle free' in fabric): prod.tags.append('wrinkle-free')
        if('performance' in fabric): prod.tags.append('wrinkle-free-ferformance')
        if('luxe wrinkle free' in fabric): prod.tags.append('luxe-wrinkle-free')
        if('plaids' in subcat or 'flannels' in subcat): prod.tags.append('plaids-and-flannels')
        if('checks' in subcat): prod.tags.append('checks-and-ginghams')
        if('prints' in subcat): prod.tags.append('prints')
        if('Solids' in subcat): prod.tags.append('solids-and-stripes')
        if(sleeve == 'Short'): prod.tags.append('short-sleeves')
        if('Tall' in subcat): prod.tags.append('tall-fit')
        if('outerwear' in subcat): prod.tags.append('outerwear')
        if(cat == 'sweaters' or cat == 'sweatshirts'): prod.tags.append('sweaters-and-sweateshirts')
        if(cat == 'polos'): prod.tags.append('Polos')
        if('Sport Coats' in subcat): prod.tags.append('sport-coats')
        if(cat == 'tees&heneleys'): prod.tags.append('tees-and-henleys')
        if('performance' in fabric): prod.tags.append('performance')
        if('pants' in subcat): prod.tags.append('pants')
        if(cat == 'shoes' or cat == 'accessories'): prod.tags.append('shoes-and-accessories')
        if(len(prod.tags) == 1): continue
        prod.vendor = 'Untuckedit-men'
        prod.collection = 'Untuckedit-men'
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

        prod.img_urls = [img['src'] for img in d['images']]
        prod.img_pos = [img['position'] for img in d['images']]

        details = d['body_html']
        size = 'Click buy for more sizing information.'
        shipping = '5-7 Business Days: Free, 2-4 Business Days: $8, 2 Business Days Guarantee: $20, Next Business Day: $25. '
        shipping += 'We accept returns of unworn, unwashed, undamaged or defective products within 30 days of the delivery date.'
        prod.body = make_body(details, size, shipping)

        tot += 1
        rows += prod.get_rows()
    i += 1
    data = json.loads(bs(get(url+str(i)).content, 'html.parser').getText())['products']
    g_total += len(data)
write_csv(file_name, rows)
print("Total products: " + str(tot) + "/" + str(g_total) + "\nTotal Time: " + str(round(time()-start, 2)) + 's')
