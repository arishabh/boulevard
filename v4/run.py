from os import listdir, path
from importlib import import_module
from time import sleep
p = path.dirname(path.abspath(__file__))
files = listdir(p)
print(files)

for i,f in enumerate(files):
    if 'reset' in f or 'template' in f or 'run' in f or 'general' in f or 'creds' in f or 'update' in f or f[-3:] != '.py': continue
    try:
        print('\n', i, '/', len(files), f)
        import_module(f[:-3])
    except Exception as e:
        print("Error:", e)
        print('\n', i, '/', len(files), f)
        sleep(10)
        import_module(f[:-3])
    print('DONE')

