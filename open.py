from os.path import getmtime, basename, splitext
from sys import argv
from glob import glob
import webbrowser
target = ''
if len(argv) < 2:
    files = glob('./images/*.jpg')
    target = max(files, key=lambda x: getmtime(x))
else:
    target = argv[1]
position = splitext(basename(target))[0]
webbrowser.open(f'https://www.google.com/maps/@{position},200m')