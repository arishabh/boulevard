from general import *

url = 'https://www.busbeemcquade.com/products.json?limit=250&page='
b = bs(get(url+'1').content, 'html.parser').getText()
data = json.loads(b)['products']
i = 2
file_name = 'BusbeeMcquadeInventory.csv'
rows = headers

while(data != []):
    for d in data:
        if(not d['variants'][0]['available']): continue
        if('men' not in d['tags']): continue
        prod = Shopify()
        prod.vendor = 'Busbee Mcquade-men'
        prod.collection = 'Busbee Mcquade-men'
        prod.title = d['title'].title()
        prod.handle = d['handle']
        prod.img_urls = [img['src'] for img in d['images']]
        prod.img_pos = [img['position'] for img in d['images']]
        var = d['variants'][0]
        prod.price = var['price']
        prod.weight = var['grams']
        prod.cap = var['compare_at_price']
        prod.sku = var['sku']
        prod.ship = var['requires_shipping']
        prod.tax = var['taxable']


        temp_tags = d['tags']
        prod.tags = [d['vendor']]
        if('new arrivals' in temp_tags): prod.tags.append('new-arrivals')
        if('tops' in temp_tags):
            prod.type = 'tops'
            prod.tags.append('tops')
        if('shorts' in temp_tags):
            prod.tags.append('shorts')
            prod.type = 'shorts'
        if('henley' in temp_tags): prod.tags.append('henley')
        if("resort-'19-men" in temp_tags): prod.tags.append("resort-'19")

        details = d['body_html']
        size = 'Click buy for more sizing information.'
        shipping = 'We are proud to offer FREE 3 Day Shipping for all orders over $99. Orders under this amount still enjoy 2 Day Shipping but are charged a flat rate of $5. Next day shipping are charged a flat rate of $20'
        shipping+='We accept returns within 30 days of your purchase for a full refund. All return items must be unworn, unwashed and undamaged with original tags still intact and in the original poly bags.'
        prod.body = make_body(details, size, shipping)
        rows += prod.get_rows()
    i += 1
    data = json.loads(bs(get(url+str(i)).content, 'html.parser').getText())['products']
write_csv(file_name, rows)
