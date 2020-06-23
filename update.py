import csv
from requests import get, put, post, delete
from time import time, sleep
from datetime import datetime, timedelta
import os
import shutil
from product import Product
from creds import base_url, top_url
import json
import sys


old_path = os.path.dirname(os.path.abspath(__file__)) + '/old/'
new_path = os.path.dirname(os.path.abspath(__file__)) + '/new/'
print(sys.argv)
run = '-nr' not in sys.argv
post_collections = '-pc' in sys.argv or '--post-collections' in sys.argv
git_pull = '-gp' in sys.argv



def csv_diff(old_csv, new_csv):
    new_prod = []
    modify_prod = []
    del_prod = []
    mode = None #False: new prod | True: modify prod 

    with open(old_path+old_csv, 'r') as old_file, open(new_path+new_csv, 'r') as new_file:
        old = list(csv.reader(old_file))[1:]
        new = list(csv.reader(new_file))[1:]

    prod = []
    for line in new:
        if line[3] == '' or not prod:
            prod.append(line)
            if line != new[-1]: continue

        old_prod = []
        mode = False
        handle = prod[0][1]
        for l in old:
            if l[1] == handle:
                mode = True
                old_prod.append(l)
            elif mode and l[3] == '': old_prod.append(l)
            elif mode and l[3] != '': break

        if not all(l in old_prod for l in prod):
            product = Product()
            product.make_product(prod)
            if not mode: 
                new_prod.append(product)
                # print("Brand new product:", prod)
            else: 
                modify_prod.append(product)
                # print("Old product\n", old_prod, "Has to be modified to\n", prod)

        for p in old_prod: old.remove(p)
        prod = [line] 
    
    if old:
        prod = []
        for line in old:
            if line[3] == '' or not prod:
                prod.append(line)
                if line != old[-1]: continue

            del_prod.append(prod[0][1])
            # print("Removed product", prod)

            prod = [line]
    
    return new_prod, modify_prod, del_prod


def get_id(handle):
    try:
        return get(base_url+'/products.json?handle='+str(handle)).json()['products'][0]['id']
    except:
        print("Couldnt find handle id: ", handle)
        return ''

def delete_prod(handle):
    prod_id = get_id(handle)
    res = delete(base_url+'/products/'+str(prod_id)+'.json').content
    # print(res, '\n\n')
    if "error" in str(res): print("Couldn't delete product with id", prod_id)

def add_prod(prod):
    data = prod.get_json()
    res = post(base_url+'/products.json', data=json.dumps(data), headers={'Content-Type': 'application/json'}).content
    # print(res, '\n\n')
    # if "error" in str(res): print("Couldn't product product with title", data['product']['title'])

def modify_prod(prod):
    prod_id = get_id(prod.handle)
    data = prod.get_json(prod_id)
    # print(json.dumps(data))
    res = put(base_url+'/products/'+str(prod_id)+'.json', data=json.dumps(data), headers={'Content-Type': 'application/json'}).content
    # print(res, '\n\n')
    if "error" in str(res): print("Couldn't product product with title", data['product']['title'])

def publish_prod(prod):
    prod_id = get_id(prod.handle)
    data = {"product_listing":{"product_id":prod_id}}
    res = put(top_url+'/product_listings/'+str(prod_id)+'.json', data=json.dumps(data), headers={'Content-Type': 'application/json'}).content
    # print(res, '\n\n')
    if "error" in str(res): print("Couldn't product product with title", data['product']['title'])

def write_file(duration, files):
    with open(os.path.dirname(os.path.abspath(__file__))+"/update_info.txt", "a+") as f:
        f.write(str((datetime.now()-timedelta(hours=-4)).strftime("%d/%m/%Y %H:%M:%S"))+" ET\n")
        f.write("Total time taken: " + str(duration/60) + ' min' + '\n')
        f.write("Total number of files: " + str(files) + "\n")
        f.write("Average time for each file: " + str(duration/files) + ' s' + "\n\n")

if __name__ == "__main__":
    start = time()
    # print(old_files)
    try:
        if run: __import__('run')
    except:
        sleep(10)
        if run: __import__('run')
    old_files = os.listdir(old_path)
    new_files = os.listdir(new_path)
    totf = 0
    for i,old in enumerate(old_files):
        try:
            new_files.index(old)
            new = old
        except:
            print("File", old, "not found in new folder")
            continue
        totf += 1
        print('\n\n' + new + " " + str(i) + '/' + str(len(old_files)) + '\n\n')
        new_prod, modify, deletes = csv_diff(old, new)
        print(len(deletes), len(modify), len(new_prod))

        for i,handle in enumerate(deletes):
            print("Deleting", handle, '|', new)
            print(str(i+1)+'/'+str(len(deletes)))
            delete_prod(handle)
            # sleep(0.2)
        for i,prod in enumerate(modify):
            print("Modifying product", prod.title, "|", new)
            print(str(i+1)+'/'+str(len(modify)))
            modify_prod(prod)
            # sleep(0.2)
        for i,prod in enumerate(new_prod): 
            print("Adding product", prod.title, '|', new)
            print(str(i+1)+'/'+str(len(new_prod)))
            add_prod(prod)
            publish_prod(prod)
            # sleep(0.2)

        os.remove(old_path+'/'+old)
        shutil.move(new_path+'/'+new, old_path+'/'+new)
    tot = time() - start
    write_file(tot, totf)
