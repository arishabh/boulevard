from os import walk
from importlib import import_module
path = '.'

for (dirpath, dirname, filenames) in walk(path):
    for f in filenames:
        if 'template' in f or 'general' in f or 'creds' in f: continue
        print('\n', f)
        import_module(f[:-3])
    break
