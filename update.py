from street_view_randomizer import main, countries
from glob import glob
from os import getenv
from os.path import getmtime, abspath
import ctypes
class SVRArgs:
    def __init__(self):
        self.api_key = getenv('GOOGLE_MAPS_API_KEY')
        self.countries = countries.countries_codes['iso3']
        self.radius = 5000
        self.list_countries = False
        self.use_area = True
        self.samples = 1
        self.output_dir = './images/'
        self.headings = [0]
        self.pitches = [0]
        self.fovs = [120]
        self.size = '640x640'

main.run(SVRArgs())
files = glob(abspath('./images/*/*.jpg'))
latest = max(files, key=lambda x: getmtime(x))
ctypes.windll.user32.SystemParametersInfoW(20, 0, latest, 0)