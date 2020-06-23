import csv
from requests import get, put, post, delete
from time import time, sleep
import os
import shutil
from product import Product
from creds import base_url, top_url
import json


old_path = 'old/'
new_path = 'new/'

def get_prods(csv):
    prods = []
    with open(new_path+csv, 'r'):
        new = list(csv.reader(new_file))[1:]
        name = new[0][4]
    prod = []
    for line in new:
        if line[3] == '' or not prod:
            prod.append(line)
            if line != new[-1]: continue
       
        p = Product()
        p.make_product(prod)
        prods.append(p)
        prod = [line] 
    
    return prods, name


def get_id(handle):
    try:
        return get(base_url+'/products.json?handle='+str(handle)).json()['products'][0]['id']
    except:
        print("Couldnt find handle id: ", handle)
        return ''

def delete_prod(handle):
    prod_id = get_id(handle)
    res = delete(base_url+'/products/'+str(prod_id)+'.json').content
    print(res, '\n\n')
    if "error" in str(res): print("Couldn't delete product with id", prod_id)

def add_prod(prod):
    data = prod.get_json()
    res = post(base_url+'/products.json', data=json.dumps(data), headers={'Content-Type': 'application/json'}).content
    print(res, '\n\n')
    # if "error" in str(res): print("Couldn't product product with title", data['product']['title'])

def publish_prod(prod):
    prod_id = get_id(prod.handle)
    data = {"product_listing":{"product_id":prod_id}}
    res = put(top_url+'/product_listings/'+str(prod_id)+'.json', data=json.dumps(data), headers={'Content-Type': 'application/json'}).content
    print(res, '\n\n')
    # if "error" in str(res): print("Couldn't product product with title", data['product']['title'])

def all_prods(name):
    

if __name__ == "__main__":
    new_files = os.listdir("./"+new_path)
    __import__('run')
    for f in new_files:
        print('\n\n' + new + '\n\n')
        prods, name = get_prods(f)

        deletes = all_prods(name)
        for i,handle in enumerate(deletes):
            print("Deleting", handle)
            print(str(i+1)+'/'+str(len(deletes)))
            delete_prod(handle)
            sleep(0.5)
        for i,prod in enumerate(new_prod): 
            print("Adding product", prod.title)
            print(str(i+1)+'/'+str(len(new_prod)))
            add_prod(prod)
            publish_prod(prod)
            sleep(0.5)

        os.remove(old_path+'/'+old)
        shutil.move(new_path+'/'+new, old_path+'/'+new)
