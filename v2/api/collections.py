from os import walk
from creds import col_url
from requests import post
path = '../scrapes'

for (dirpath, dirname, filenames) in walk(path):
    for f in filenames:
        if 'template' in f or 'general' in f

    break
