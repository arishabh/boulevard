from os import listdir, path
from importlib import import_module
from time import sleep
path = path.dirname(path.abspath(__file__))
files = listdir(path)

for i,f in enumerate(files):
    if 'reset' in f or 'template' in f or 'run' in f or 'general' in f or 'creds' in f or 'update' in f or f[-3:] != '.py': continue
    print('\n', i, '/', len(files), f)
    try:
        import_module(f[:-3])
    except:
        sleep(20)
        import_module(f[:-3])

