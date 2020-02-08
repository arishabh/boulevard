from requests import get
from bs4 import BeautifulSoup as bs
import json
import re
from time import time
import csv

headers  = [['Collection', 'Handle', 'Title', 'Body (HTML)', 'Vendor', 'Type', 'Tags', 'Published', 'Option1 Name', 'Option1 Value', 'Option2 Name', 'Option2 Value', 'Option3 Name', 'Option3 Value', 'Variant SKU', 'Variant Grams', 'Variant Inventory Tracker', 'Variant Inventory Policy', 'Variant Fulfillment Service', 'Variant Price', 'Variant Compare At Price', 'Variant Requires Shipping', 'Variant Taxable', 'Variant Barcode', 'Image Src', 'Image Position', 'Image Alt Text', 'Gift Card', 'SEO Title', 'SEO Description', 'Google Shopping / Google selfuct Category', 'Google Shopping / Gender', 'Google Shopping / Age Group', 'Google Shopping / MPN', 'Google Shopping / AdWords Grouping', 'Google Shopping / AdWords Labels', 'Google Shopping / Condition', 'Google Shopping / Custom Product', 'Google Shopping / Custom Label 0', 'Google Shopping / Custom Label 1', 'Google Shopping / Custom Label 2', 'Google Shopping / Custom Label 3', 'Google Shopping / Custom Label 4', 'Variant Image', 'Variant Weight Unit', 'Variant Tax Code', 'Cost per item']]
class Shopify:
    def __init__(self, d='', c='', name=''):
        url = ['https://'+name+'.com/collections/',  '/products.json?limit=250&page=']
        self.collection = ''
        self.handle = ''
        self.title = ''
        self.body = ''
        self.vendor = ''
        self.type = ''
        self.tags = ''
        self.published = ''
        self.option1_name = 'Title'
        self.option1_value = 'Default Title'
        self.option2_name = 'Link'
        self.link = ''
        self.option3_name = ''
        self.option3_value = ''
        self.sku = ''
        self.weight = ''
        self.inv_tracker = ''
        self.policy = 'deny'
        self.full_service = 'manual'
        self.price = ''
        self.cap = ''
        self.ship = ''
        self.tax = ''
        self.barcode = ''
        self.img_urls = []
        self.img_pos = []
        self.img_alt_text = ''
        self.gift_card = 'FALSE'
        self.seo_title = ''
        self.seo_desc = ''
        self.google_ship = ['']*13
        self.var_img = ''
        self.var_weight_unit = ''
        self.variant_tax = ''
        self.cost_item = ''

        self.vendor = name+'-men'
        self.collection = name+'-men'
        self.title = d['title']
        self.handle = d['handle']
        self.type = d['product_type'].lower()

        var = d['variants'][0]
        self.price = var['price']
        self.weight = var['grams']
        self.tax = var['taxable']
        self.ship = var['requires_shipping']
        self.sku = var['sku']
        self.cap = var['compare_at_price']
        self.link = url[0]+c+'/products/'+self.handle

        self.img_urls = [img['src'] for img in d['images']]
        self.img_pos = [img['position'] for img in d['images']]

    def get_first_row(self):
        self.tags = ', '.join(self.tags)
        out = [self.collection, self.handle, self.title, self.body, self.vendor, self.type, self.tags, self.published, self.option1_name, self.option1_value, self.option2_name, self.link, self.option3_name]
        out += [self.option3_value, self.sku, self.weight, self.inv_tracker, self.policy, self.full_service, self.price, self.cap, self.ship, self.tax, self.barcode, self.img_urls[0], self.img_pos[0]]
        out += [self.img_alt_text, self.gift_card, self.seo_title, self.seo_desc] + self.google_ship + [self.var_img, self.var_weight_unit, self.variant_tax, self.cost_item]
        return [out]

    def get_other_rows(self):
        rows = []
        for i in range(len(self.img_urls[1:])):
            rows.append([self.collection, self.handle] + (['']*22) + [self.img_urls[i+1], self.img_pos[i+1]])
        return rows

    def get_rows(self):
        return(self.get_first_row() + self.get_other_rows())

    def __eq__(self, other):
        return self.title == other.title


def write_csv(file_name, rows):
    with open(file_name, 'w+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

def clean_text(text):
    cleanr = re.compile('<.*?>')
    text = re.sub(cleanr, '', text)
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", text).split())

def make_body(det, size, ship):
    out = '<sections><section id="1"><sectionTitle>Details</sectionTitle><sectionBody>' + clean_text(det) +'</sectionBody></section>'
    out += '<section id="2"><sectionTitle>Size &amp; Fit</sectionTitle><sectionBody>'+ size +'</sectionBody></section>'
    out += '<section id="3"><sectionTitle>Shipping &amp; Returns</sectionTitle><sectionBody>'+ ship +'</sectionBody></section></sections>'
    return out

def list_new(li):
    d = {}
    sub = []
    fab = []
    for elem in li:
        e = elem.split(':')
        if(len(e) == 1):
            sub.append(e[0])
        elif(e[0] == 'subcat'):
            sub.append(e[1])
        elif(e[0] == 'fabric'):
            fab.append(e[1])
        else:
            d[e[0]] = e[1]
    d['subcat'] = sub
    d['fabric'] = fab
    return d

def others(url, self, d, c, vendor):
    self.vendor = vendor+'-men'
    self.collection = vendor+'-men'
    self.title = d['title']
    self.handle = d['handle']
    self.type = d['product_type'].lower()

    var = d['variants'][0]
    self.price = var['price']
    self.weight = var['grams']
    self.tax = var['taxable']
    self.ship = var['requires_shipping']
    self.sku = var['sku']
    self.cap = var['compare_at_price']
    self.link = url[0]+c+'/products/'+self.handle

    self.img_urls = [img['src'] for img in d['images']]
    self.img_pos = [img['position'] for img in d['images']]

def gen_clean(text):
    text = text.split('-1')[0]
    return text.lower().replace(' ', '-')

def gen_clean_li(li):
    return list(map(gen_clean, li))

def check(d):
    out = 'gift' in d['title'].lower() or 'gift' in d['handle'].lower() or 'gift' in d['product_type']
    out = out or not any([v['available'] for v in d['variants']])
    out = out or 'women' in d['tags'] or 'womens' in d['tags']
    out = out or d['tags'] == []
    return out
