from requests import get, post
from product import Product
from time import time
import json
from bs4 import BeautifulSoup as bs
import re
from time import time
from datetime import datetime
import csv
from creds import col_url
from urllib.request import urlopen
from PIL import Image


class Shopify():
    def __init__(self, name, display_name, cats, shipping, note=''):
        self.note = 'Welcome to V3\n'+note
        self.name = name
        self.dname = display_name
        self.cats = cats
        self.shipping = shipping
        self.size = 'Click buy for more sizing information.'
        self.file_name = self.name.title() + 'Inventory.csv'
        self.url = ['https://' + self.name + '.com/collections/', '/products.json?limit=250&page=']
        self.link = self.url[0].split('collections')[0]
        self.reason = {'"Gift" in product': 0, 'No images': 0, 'Tags empty': 0, 'Women product': 0, 'Repeated product': 0}
        self.prods = []
        self.csv_path = 'csv/'
        self.info_path = 'info/'
        self.headers  = [['Collection', 'Handle', 'Title', 'Body (HTML)', 'Vendor', 'Type', 'Tags', 'Published', 'Option1 Name', 'Option1 Value', 'Option2 Name', 'Option2 Value', 'Option3 Name', 'Option3 Value', 'Variant SKU', 'Variant Grams', 'Variant Inventory Tracker', 'Variant Inventory Policy', 'Variant Fulfillment Service', 'Variant Price', 'Variant Compare At Price', 'Variant Requires Shipping', 'Variant Taxable', 'Variant Barcode', 'Image Src', 'Image Position', 'Image Alt Text', 'Gift Card', 'SEO Title', 'SEO Description', 'Google Shopping / Google selfuct Category', 'Google Shopping / Gender', 'Google Shopping / Age Group', 'Google Shopping / MPN', 'Google Shopping / AdWords Grouping', 'Google Shopping / AdWords Labels', 'Google Shopping / Condition', 'Google Shopping / Custom Product', 'Google Shopping / Custom Label 0', 'Google Shopping / Custom Label 1', 'Google Shopping / Custom Label 2', 'Google Shopping / Custom Label 3', 'Google Shopping / Custom Label 4', 'Variant Image', 'Variant Weight Unit', 'Variant Tax Code', 'Cost per item']]
        self.rows = self.headers
        self.tot = 0

    def run(self):
        self.start = time()
        for c in self.cats:
            ind = 1
            self.data = json.loads(bs(get(self.url[0] + c + self.url[1] + '1').content, 'html.parser').getText())[
                'products']  # For each category in given in above, get its json
            while self.data:
                for d in self.data:
                    self.d = d
                    err, self.reason = self.check()
                    if err: continue
                    self.colors, self.fits, self.pos, self.all_sizes = self.get_color_fit(d)

                    for color in self.colors:
                        if color != '' and self.pos[color] == [0]: continue
                        for fit in self.fits:
                            self.prod = Product(self.d, c, self.name, self.dname, self.link)

                            if color is not '':
                                self.add_color(color)

                            if fit != '': 
                                self.add_fit(fit)

                            if self.check_error(): continue 

                            self.process_sizes(color, fit)

                            details = clean_text(d['body_html'])  # See the body_html from the product and clean it
                            self.prod.body = make_body(details, self.size, self.shipping)
            
                            self.tot += 1
                            self.prods.append(self.prod)
                            self.rows += self.prod.get_rows()
                ind += 1
                self.data = json.loads(bs(get(self.url[0] + c + self.url[1] + str(ind)).content, 'html.parser').getText())['products']
            if ind == 1: print("No products in category " + c)
        print("Total products: " + str(self.tot) + "/" + str(sum(list(self.reason.values())) + self.tot) + "\nTotal Time: " + str(round(time() - self.start, 2)) + 's')
        if sum(list(self.reason.values())) != 0: print(str(self.reason))

    def get_color_fit(self, d):
        colors = []
        all_sizes = []
        fits = []
        waist = []
        length = []
        for option in d['options']:
            if (option['name'].lower() == 'color'):
                colors = option['values']
            elif ('size' in option['name'].lower()):
                all_sizes = option['values']
            elif (option['name'].lower() == 'fit' or option['name'] == "Style"):
                fits = option['values']
            elif ('waist' in option['name'].lower()):
                waist = option['values']
            elif ('length' in option['name'].lower()):
                length = option['values']
            else:
                print("Couldnt find list for option", option['name'], "with info", option['values'])
        if length == []: length = ['']
        for w in waist:
            for l in length:
                all_sizes.append(w + " / " + l) if l != '' else all_sizes.append(w)
        if all_sizes == []: all_sizes = ['OS']
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
                    pos[p] = range(20)
            lims = list(pos.values())
            for i in range(len(lims)):
                try:
                    if (len(lims[i]) != 1): continue
                    list.sort(lims[i + 1])
                    lims[i] += range(lims[i][0] + 1, lims[i + 1][0])
                except:
                    for _ in range(5):
                        lims[i].append(lims[i][-1] + 1)
        else:
            colors = ['']
        
        return colors, fits, pos, all_sizes

    def add_color(self, color):
        self.prod.title += ' - ' + color
        self.prod.handle += '-' + gen_clean(color)
        self.prod.img_pos = []
        self.prod.img_urls = []
        for img in self.d['images']:
            if (img['position'] in self.pos[color]):
                self.prod.img_urls.append(img['src'])
                self.prod.img_pos.append(len(self.prod.img_urls))

    def add_fit(self, fit):
        self.prod.title += ' - ' + fit
        self.prod.handle += '-' + gen_clean(fit)
    
    def process_sizes(self, color, fit):
        avail_sizes = []
        for v in self.d['variants']:
            if color in v['title'] and fit in v['title']:
                if (color or fit) and not avail_sizes: self.prod.link += str(v["id"])
                if self.all_sizes == ['OS']: size = 'OS'
                else: size = list(filter(lambda x: all(map(lambda a: a in v['title'], x.split('/'))), self.all_sizes))[0]
                if v['available'] and size not in avail_sizes: avail_sizes.append(size)
        proc_all_sizes = self.proc_size_li(self.all_sizes)
        proc_avail_sizes = self.proc_size_li(avail_sizes)
        self.prod.write_sizes(proc_all_sizes, proc_avail_sizes)

    def proc_size(self, size):
        size = size.upper().replace('-', '')
        if 'O/S' in size or 'OS' in size or ('O' in size and 'S' in size): return 'OS'
        elif 'XS' in size or 'XSMALL' in size: return 'XS'
        elif 'S' in size or 'SMALL' in size: return 'S'
        elif 'M' in size or 'MEDIUM' in size: return 'M'
        elif 'L' in size or 'LARGE' in size: return 'L'
        elif 'XL' in size or 'XLARGE' in size: return 'XL'
        elif 'XXL' in size or 'XXLARGE' in size: return 'XXL'
        elif 'XXXL' in size or 'XXXLARGE' in size: return 'XXXL'
        else:
            #print("Size not found for", size)
            return size

    def proc_size_li(self, li):
        return list(set(map(self.proc_size, li)))

    def check(self):
        out = 'gift' in self.d['title'].lower() or 'gift' in self.d['handle'].lower() or 'gift' in self.d['product_type']
        if out: self.reason['"Gift" in product'] += 1
        out1 = False
        # out1 = not any([v['available'] for v in d['variants']])
        # if out1: reason['Sold out'] += 1
        out2 = 'women' in self.d['tags'] or 'womens' in self.d['tags'] or 'women' in self.d['handle'] or 'women' in self.d['product_type'] or 'women' in self.d['title']
        if out2: self.reason['Women product'] += 1
        out3 = self.d['tags'] == []
        if out3: self.reason['Tags empty'] += 1
        return (out or out1 or out2 or out3), self.reason

    def write_info(self):
        tot = "Total products: " + str(self.tot) + "/" + str(sum(list(self.reason.values()))+self.tot)
        time_info = "Total Time: " + str(round(time()-self.start, 2)) + 's'
        with open(self.info_path+self.name.title()+'.txt', "a+") as f:
            f.writelines([str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))+'\n', self.note+'\n', tot+'\n', time_info+'\n', str(self.reason)+'\n', '\n\n'])

    def write_csv(self):
        with open(self.csv_path+self.file_name, 'w+') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.rows)

    def post_collections(self):
        if not self.cats or self.cats == ['']: 
            image = self.img_finder(None)
            data = {"smart_collection":{"title": self.dname+'-men:All', "rules":[{"column":"vendor", "relation":"contains", "condition":self.name+"-men"}], "image":{"src":image}}}
            a = post(col_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            print(a.content)
            return

        for c in self.cats:
            image = self.img_finder(gen_clean(c))
            print(image)
            if not image: continue
            data = {"smart_collection":{"title": self.dname+'-men:'+self.fancy(c), "rules":[{"column":"vendor", "relation":"contains", "condition":self.name+"-men"}, {"column":"tag", "relation":"equals", "condition":gen_clean(c)}], "disjunctive": False, "image":{"src":image, "alt":gen_clean(c)}}} 
            a = post(col_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            print(a.content)

    def img_finder(self, find):
        url = None
        with open(self.csv_path+self.file_name, "r") as f:
            reader = csv.reader(f)
            for r in reader:
                if r[6] == ''or r[6] == 'Tags': continue
                if find and find != r[6].split(',')[1].strip(): continue
                if('.jpg' in r[24]):
                    url = r[24].split('.jpg')[0]+'_350x350.jpg' + r[24].split('.jpg')[1]
                    return url
                elif('.png' in r[24]):
                    url = r[24].split('.png')[0]+'_350x350.png' + r[24].split('.png')[1]
                    return url

    def check_error(self):    
        if (self.prod in self.prods):
            self.reason['Repeated product'] += 1
            return True
        if not self.prod.img_urls: 
            self.reason["No images"] += 1
            return True

    def fancy(self, text):
        return text.replace('-', ' ').title()

def clean_text(text):
    text.replace('\n', '.')
    cleanr = re.compile('<.*?>')
    text = re.sub(cleanr, '', text)
    text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", text).split())
    text = re.sub('[^A-Za-z0-9]+', ' ', text)
    if 'window' in text.split(): text = ' '.join(text.split()[:text.split().index('window')])
    return text

def make_body(det, size, ship):
    out = '<sections><section id="1"><sectionTitle>Details</sectionTitle><sectionBody>' + clean_text(det) +'</sectionBody></section>'
    out += '<section id="2"><sectionTitle>Size &amp; Fit</sectionTitle><sectionBody>'+ size +'</sectionBody></section>'
    out += '<section id="3"><sectionTitle>Shipping &amp; Returns</sectionTitle><sectionBody>'+ ship +'</sectionBody></section></sections>'
    return out


def gen_clean(text):
    text = text.split('-1')[0]
    text = text.lower().replace(' ', '-')
    text = text.replace('/', '-')
    text = text.replace("'", '')
    text = re.sub('[^A-Za-z0-9]+', ' ', text)
    return text

def gen_clean_li(li):
    return list(map(gen_clean, li))

