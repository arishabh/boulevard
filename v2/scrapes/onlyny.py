## Dont change, initializing constants
##############
from general import *
start = time() #Timing this program
i=2 #setting the index for the page number in the url end
tot = 0 #Number of products selected
prods = [] #All products
rows = headers
reason = {'"Gift" in product': 0, 'Sold out': 0, 'Tags empty': 0, 'Women product': 0, 'Repeated product': 0}
##############

# Add data here, name of company, the catagories as per the url and the tags you want to check for
# Some general tags have been already added, add onto them
NAME = 'onlyny' #e.g. onlyny | Has to be the same as on url
DISPLAY_NAME = 'OnlyNY'
cats = ['new-arrivals', 'tees', 'tops', 'bottoms', 'outerwear', 'sweatshirts', 'swim-shorts', 'accessories']
note = 'Added display name for vendor and collection'

file_name = NAME.title()+'Inventory.csv'
url = ['https://'+ NAME +'.com/collections/',  '/products.json?limit=250&page=']

for c in cats:
    ind = 1
    data = json.loads(bs(get(url[0]+c+url[1]+'1').content, 'html.parser').getText())['products'] # For each catagory in given in above, get its json
    while(data != []):
        for d in data:
            err, reason = check(d, reason)
            if(err): continue
            for option in d['options']:
                if(option['name'] == 'Color'): colors = option['values']
                elif(option['name'] == 'Size'): all_sizes = option['values']
            pos = {}
            for color in colors: pos[color] = []
            for v in d['variants']:
                if not v: continue
                try:
                    if v['featured_image']['position'] not in pos[v['option1']]: 
                        pos[v['option1']].append(v['featured_image']['position'])
                except:
                    continue
            pos = {k: v for k, v in sorted(pos.items(), key=lambda item: item[1])} 
            lims = list(pos.values())
            for i in range(len(lims)):
                try:
                    if(len(lims[i]) != 1): continue
                    list.sort(lims[i+1])
                    for j in range(lims[i][0]+1, lims[i+1][0]):
                        lims[i].append(j)
                except Exception as e:
                    for j in range(20):
                        lims[i].append(lims[i][-1]+1)
            
            for color in colors:
                prod = Shopify(d, c, NAME, DISPLAY_NAME) #Intialize Shopify product 
                prod.title += ' - ' + color
                prod.handle += '-' + gen_clean(color)
                prod.img_pos = []
                prod.img_urls = []
                for img in d['images']:
                    if(img['position'] in pos[color]):
                        prod.img_urls.append(img['src'])
                        prod.img_pos.append(len(prod.img_urls))

                avail_sizes = []
                for v in d['variants']:
                    if(v['option1'] != color): continue
                    size = v['option2']
                    if size == None or size == 'O/S': size = 'OS'
                    if v['available'] and size not in avail_sizes: avail_sizes.append(size)
                prod.write_sizes(all_sizes, avail_sizes)


                details = clean_text(d['body_html']) #See the body_html from the product and clean it
                size = 'Click buy for more sizing information.'
                #Add the the shipping and return details below
                shipping = 'Most Orders Are Processed And Shipped Within 1-2 Business Days Of Purchase However Please Allow Up To 5 Business Days For Processing All Orders Are Shipped From New York City And Delivery Time Is Based On Shipping Method.'
                shipping += 'Full priced items purchased from onlyny.com are eligible for a full refund or exchange if returned within 30 days of purchase. Any already marked down items are not eligible for return, but can be exchanged for anything else on the website.'
                prod.body = make_body(details, size, shipping)

                if(prod in prods): #Check if this product has already been seen
                    reason['Repeated product'] += 1
                    continue
                prods.append(prod)
                if not prod.img_urls: continue
                rows += prod.get_rows()
            tot += 1
        ind += 1
        data = json.loads(bs(get(url[0] + c + url[1] + str(ind)).content, 'html.parser').getText())['products']
    if ind == 1: print("No products for category " + c)
write_csv(file_name, rows)
print("Total products: " + str(tot) + "/" + str(sum(list(reason.values())) + tot) + "\nTotal Time: " + str(
    round(time() - start, 2)) + 's')
if sum(list(reason.values())) != 0: print(str(reason))
write_file(NAME.title(), "Total products: " + str(tot) + "/" + str(sum(list(reason.values()))+tot), "Total Time: " + str(round(time()-start, 2)) + 's', reason, note)
post_collections(NAME, DISPLAY_NAME, cats)
