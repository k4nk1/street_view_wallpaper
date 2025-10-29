from os.path import getmtime, basename, splitext, dirname
from os import chdir
from sys import argv
from glob import glob
import webbrowser
chdir(dirname(__file__))
target = ''
if len(argv) < 2:
    files = glob('./images/*/*.jpg')
    target = max(files, key=lambda x: getmtime(x))
else:
    target = argv[1]
position = splitext(basename(target))[0]
webbrowser.open(f'https://www.google.com/maps/@{position},200m')