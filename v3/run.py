from os import listdir
from importlib import import_module
path = '.'

for f in listdir(path):
    if 'template' in f or 'general' in f or 'creds' in f or 'update' in f or f[-3:] != '.py': continue
    print('\n', f)
    import_module(f[:-3])
