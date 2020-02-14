import re

class Product:
    def __init__(self, d='', c='', name='', display_name='', url = ''):
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
        self.option3_name = 'Sizes'
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

        self.vendor = display_name+'-men'
        # self.collection = display_name+'-men'
        self.title = d['title']
        self.handle = d['handle']
        self.type = d['product_type'].lower()

        var = d['variants'][0]
        self.price = var['price']
        self.weight = var['grams']
        self.tax = var['taxable']
        self.ship = var['requires_shipping']
        # self.sku = var['sku']
        self.cap = var['compare_at_price']
        self.link = url + 'products/'+self.handle

        self.img_urls = [img['src'] for img in d['images']]
        self.img_pos = [img['position'] for img in d['images']]
        
        self.tags = [gen_clean(d['vendor']), gen_clean(c)] + gen_clean_li(d['tags'])

    def get_first_row(self):
        tags = ', '.join(self.tags)
        out = [self.collection, self.handle, self.title, self.body, self.vendor, self.type, tags, self.published, self.option1_name, self.option1_value, self.option2_name, self.link, self.option3_name]
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

    def write_sizes(self, all_sizes, avail_sizes):
        self.option3_value = ','.join(avail_sizes)

    def __eq__(self, other):
        return (self.title == other.title and self.handle == other.handle)

def gen_clean(text):
    text = text.split('-1')[0]
    text = text.lower().replace(' ', '-')
    text = text.replace('/', '-')
    text = text.replace("'", '')
    text = re.sub('[^A-Za-z0-9]+', ' ', text)
    return text

def gen_clean_li(li):
    return list(map(gen_clean, li))
