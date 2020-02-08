from general import *

NAME = 'thenormalbrand'
start = time()
tot = 0
url = ['https://thenormalbrand.com/collections/',  '/products.json?limit=250&page=']
cats = ['outerwear', 'hats', 'accessories', 'sweaters-pullovers', 'button-up-shirts', 't-shirts', 'henleys', 'pants', 'new', 'bestseller', 'shirts']
check_tags = ['bottoms', 'shorts', 'shirt', 'jacket', 'hoodie', 'bag', 'bundle', 'beanie', 'dad-cap', 'joggers', 'jogger', 'canvas-pants', 'chino', 'henley', 'jacket', 'shirt-jacket', 'pullover', 'button-down', 'vest', 'hats', 'button-up']
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
            if(all_check(d)): continue
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

            details = clean_text(d['body_html'])
            size = 'Click buy for more sizing information.'
            shipping = 'Returns and exchanges for unwashed and unworn items in original condition will be accepted up to 30 days from the date of purchase.'
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
