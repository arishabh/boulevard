## Dont change, initializing constants
##############
from general import *
start = time() #Timing this program
i=2 #setting the index for the page number in the url end
g_tot = 0 #Total number of products scraped aka Grand_Total
tot = 0 #Number of products selected
prods = [] #All products
rows = headers
reason = {'"Gift" in product': 0, 'Sold out': 0, 'Tags empty': 0, 'Women product': 0, 'Repeated product': 0}
##############

# Add data here, name of company, the catagories as per the url and the tags you want to check for
# Some general tags have been already added, add onto them
NAME = 'corridornyc' #e.g. onlyny | Has to be the same as on url
DISPLAY_NAME = 'Corridor'
cats=['shirts', 'outerwear', 'sweaters', 't-shirt', 'bottoms', 'suits', 'accessories-1', 'new-arrivals-1', 'friends-of-friends', 'things-theyll-need', 'city-rustic', 'clean-and-classy', 'modern-minimalist']
note = 'Added display name for vendor and collection'

file_name = NAME.title()+'Inventory.csv'
url = ['https://'+ NAME +'.com/collections/',  '/products.json?limit=250&page=']

# Add code in function to process each size
def proc_size(size):
    size = size.split('/ ')[-1]
    if(size == 'One Size'): return 'OS'
    if(size == 'N/A'): return 'OS'
    return size

for c in cats:
    ind = 1
    data = json.loads(bs(get(url[0]+c+url[1]+'1').content, 'html.parser').getText())['products'] # For each catagory in given in above, get its json
    while(data != []):
        for d in data:
            err, reason = check(d, reason)
            if(err): continue
            prod = Shopify(d, c, NAME, DISPLAY_NAME) #Intialize Shopify product 

            avail_sizes = []
            all_sizes = []
            for v in d['variants']:
                size = proc_size(v['title'])
                if v['available'] and size not in avail_sizes: avail_sizes.append(size)
                if size not in all_sizes: all_sizes.append(size)
            prod.write_sizes(all_sizes, avail_sizes)

            details = clean_text(d['body_html']) #See the body_html from the product and clean it
            size = 'Click buy for more sizing information.'
            #Add the the shipping and return details below
            shipping = ''
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
