##############
## Dont change, initializing constants
from general import *
start = time() #Timing this program
i=2 #setting the index for the page number in the url end
g_total = 0 #Total number of products scraped aka Grand_Total
tot = 0 #Number of products selected
prods = [] #All products
rows = headers
##############

# Add data here, name of company, the catagories as per the url and the tags you want to check for
# Some general tags have been already added, add onto them
NAME = ''
cats = []
check_tags = ['pants', 'pant', 'shirts', 'shirt', 't-shirts', 't-shirt', 'tshirt', 'tshirts', 'sweatshirts', 'sweatshirt', 'new-arrivals', 'new-arrival', 'outerwear']

file_name = NAME.title()+'Inventory.csv'
url = ['https://'+ NAME +'.com/collections/',  '/products.json?limit=250&page=']

for c in cats:
    data = json.loads(bs(get(url[0]+c+url[1]+'1').content, 'html.parser').getText())['products'] # For each catagory in given in above, get its json
    g_total += len(data)
    while(data != []):
        for d in data:
            if(check(d)): continue
            prod = Shopify(d, c, NAME) #Intialize Shopify product 
            prod.tags = [gen_clean(d['vendor']), gen_clean(c)] #Set the prosucts to be the vendor and the catagory by default

            all_tags = gen_clean_li(d['tags']) #See the tags given in the products
            #Iterate through the catagories and add if it is in the tags given by the product
            prod.tags += [a for a in (cats+check_tags) if(a in all_tags and a not in prod.tags)]

            details = clean_text(d['body_html']) #See the body_html from the product and clean it
            size = 'Click buy for more sizing information.'
            #Add the the shipping and return details below
            shipping = ''
            prod.body = make_body(details, size, shipping)

            if(prod in prods): continue #Check if this product has already been seen
            tot += 1
            prods.append(prod)
            rows += prod.get_rows()
        i += 1
        data = json.loads(bs(get(url[0]+c+url[1]+str(i)).content, 'html.parser').getText())['products']
        g_total += len(data)
write_csv(file_name, rows)
print("Total products: " + str(tot) + "/" + str(g_total) + "\nTotal Time: " + str(round(time()-start, 2)) + 's')
