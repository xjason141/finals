#!/usr/bin/env python3

import requests
import os
from PIL import Image

#Shows how a file can be uploaded using the Python requests module

url = 'http://localhost/upload/'
# with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
#     r = requests.post(url, files={'file': opened})

img_path = 'catalog-updater/supplier-data/images'

for files in os.listdir(img_path):
    if files.endswith('jpeg'):
        with open(img_path + '/' + files, 'rb') as pics:
            r = requests.post(url, files={'file': pics})