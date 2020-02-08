from general import *

NAME = 'bearbottomclothing'
DISPLAY_NAME = 'Bearbottom'
start = time()
tot = 0
url = ['https://bearbottomclothing.com/collections/',  '/products.json?limit=250&page=']
cats=['7-run-shorts', '5-5-rec-shorts', '7-rec-shorts', '5-5-run-shorts', '7-drifter-shorts', '5-5-stretch-shorts', '7-stretch-shorts', '7-easy-shorts', '8-hybrid-shorts', '8-sateen-shorts', '7-drawstring-shorts', 'swim', 'tech-tee', 'core-tee', 'outerwear', 'paracord-bracelets', 'gear']
note = 'Added display name for vendor and collection'
i=2
file_name = NAME.title()+'Inventory.csv'
rows = headers
prods = []
reason = {'"Gift" in product': 0, 'Sold out': 0, 'Tags empty': 0, 'Women product': 0, 'Repeated product': 0}
avail_size = []
all_size = []

def proc_size(size):
    size = size.split(' / ')[0]
    if(size == 'Default Title'): return 'OS'
    return size

for c in cats:
    ind = 1
    b = bs(get(url[0]+c+url[1]+'1').content, 'html.parser').getText()
    data = json.loads(b)['products']
    while(data != []):
        for d in data:
            err, reason = check(d, reason)
            if(err): continue
            prod = Shopify(d, c, NAME, DISPLAY_NAME)

            for v in d['variants']:
                size = proc_size(v['title'])
                if v['available'] and size not in avail_size: avail_size.append(size)
                if size not in all_size: all_size.append(size)
            prod.write_sizes(all_size, avail_size)

            details = clean_text(d['body_html'])
            size = 'Click buy for more sizing information.'
            shipping = 'We offer FREE standard shipping in the US on all orders $99+. $5 standard shipping on all other orders. Most orders ship out the next business day. Some even go out the same day.'
            shipping += 'We offer free exchanges within 30 days of placing your order for unworn and unwashed products. We can not accept any international returns or exchanges.'
            prod.body = make_body(details, size, shipping)

            if(prod in prods): #Check if this product has already been seen
                reason['Repeated product'] += 1
                continue
            tot += 1
            prods.append(prod)
            rows += prod.get_rows()
        ind += 1
        data = json.loads(bs(get(url[0] + c + url[1] + str(ind)).content, 'html.parser').getText())['products']
    if ind == 1: print("No products for category " + c)
write_csv(file_name, rows)
print("Total products: " + str(tot) + "/" + str(sum(list(reason.values())) + tot) + "\nTotal Time: " + str(
    round(time() - start, 2)) + 's')
if sum(list(reason.values())) != 0: print(str(reason))
write_file(NAME.title(), "Total products: " + str(tot) + "/" + str(sum(list(reason.values()))+tot), "Total Time: " + str(round(time()-start, 2)) + 's', reason, note)
post_collections(NAME, DISPLAY_NAME, cats)
