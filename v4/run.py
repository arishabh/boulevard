from os import listdir
from importlib import import_module
path = '.'
files = listdir(path)

for i,f in enumerate(files):
    if 'reset' in f or 'template' in f or 'run' in f or 'general' in f or 'creds' in f or 'update' in f or f[-3:] != '.py': continue
    print('\n', i, '/', len(files), f)
    import_module(f[:-3])
