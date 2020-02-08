## Dont change, initializing constants
##############
from general import *

start = time()  # Timing this program
i = 2  # setting the index for the page number in the url end
tot = 0  # Number of products selected
prods = []  # All products
rows = headers
reason = {'"Gift" in product': 0, 'Sold out': 0, 'Tags empty': 0, 'Women product': 0, 'Repeated product': 0}
##############

# Add data here, name of company, the catagories as per the url and the tags you want to check for
# Some general tags have been already added, add onto them
NAME = 'tenthousand'  # e.g. onlyny | Has to be the same as on url (lowercase)
DISPLAY_NAME = 'Ten Thousand'
cats = ['']
# Add the the shipping and return details below
shipping = 'Free shipping. Free returns'
note = 'Changed the URl (with https)'

file_name = NAME.title() + 'Inventory.csv'
url = 'https://www.' + NAME + '.cc/products.json?limit=250&page='

for c in cats:
    ind = 1
    data = json.loads(bs(get(url + '1').content, 'html.parser').getText())[
        'products']  # For each catagory in given in above, get its json
    while data:
        for d in data:
            err, reason = check(d, reason)
            if err: continue
            colors = []
            all_sizes = []
            fits = []
            for option in d['options']:
                if (option['name'] == 'Color'):
                    colors = option['values']
                elif (option['name'] == 'Size'):
                    all_sizes = option['values']
                elif (option['name'] == 'Fit'):
                    fits = option['values']
            if len(all_sizes) < 2: all_sizes = ['OS']
            if len(fits) < 2: fits = ['']
            pos = {}
            if len(colors) > 2:
                for color in colors: pos[color] = []
                for v in d['variants']:
                    color = list(filter(lambda x: x in v['title'], colors))[0]
                    if v['featured_image'] == None:
                        pos[color] = [0]
                        continue
                    if v['featured_image']['position'] not in pos[color]:
                        pos[color].append(v['featured_image']['position'])
                pos = {k: v for k, v in sorted(pos.items(), key=lambda item: item[1])}
                if all(map(lambda x: x == [0], list(pos.values()))):
                    for p in pos:
                        pos[p] = [_ for _ in range(20)]
                lims = list(pos.values())
                for i in range(len(lims)):
                    try:
                        if (len(lims[i]) != 1): continue
                        list.sort(lims[i + 1])
                        lims[i] += range(lims[i][0] + 1, lims[i + 1][0])
                    except Exception as e:
                        for j in range(20):
                            lims[i].append(lims[i][-1] + 1)
            else:
                colors = ['']

            for color in colors:
                for fit in fits:
                    prod = Shopify(d, c, NAME, DISPLAY_NAME)  # Intialize Shopify product
                    if color is not '':
                        prod.title += ' - ' + color
                        prod.handle += '-' + gen_clean(fit)
                        prod.img_pos = []
                        prod.img_urls = []
                        for img in d['images']:
                            if (img['position'] in pos[color]):
                                prod.img_urls.append(img['src'])
                                prod.img_pos.append(len(prod.img_urls))

                    if fit != '': 
                        prod.title += ' - ' + fit
                        prod.handle += '-' + gen_clean(fit)

                    if not prod.img_urls: continue

                    avail_sizes = []
                    for v in d['variants']:
                        if color in v['title'] and fit in v['title']:
                            if all_sizes == ['OS']: size = 'OS'
                            else:
                                size = list(filter(lambda x: x in v['title'], all_sizes))[0]
                        if v['available'] and size not in avail_sizes: avail_sizes.append(size)
                    all_sizes = proc_size_li(all_sizes)
                    avail_sizes = proc_size_li(avail_sizes)
                    prod.write_sizes(all_sizes, avail_sizes)

                    details = clean_text(d['body_html'])  # See the body_html from the product and clean it
                    size = 'Click buy for more sizing information.'
                    # Add the the shipping and return details below
                    shipping = 'Returns and exchanges for unwashed and unworn items in original condition will be accepted up to 30 days from the date of purchase.'
                    prod.body = make_body(details, size, shipping)

                    if (prod in prods):  # Check if this product has already been seen
                        reason['Repeated product'] += 1
                        continue
                    tot += 1
                    prod.link = 'https://www.tenthousand.cc/products/'+prod.handle
                    prods.append(prod)
                    rows += prod.get_rows()
        ind += 1
        data = json.loads(bs(get(url + str(ind)).content, 'html.parser').getText())['products']
    if ind == 1: print("No products for category " + c)
write_csv(file_name, rows)
print("Total products: " + str(tot) + "/" + str(sum(list(reason.values())) + tot) + "\nTotal Time: " + str(
    round(time() - start, 2)) + 's')
if sum(list(reason.values())) != 0: print(str(reason))
write_file(NAME.title(), "Total products: " + str(tot) + "/" + str(sum(list(reason.values()))+tot), "Total Time: " + str(round(time()-start, 2)) + 's', reason, note)
post_collections(NAME, DISPLAY_NAME, cats)
