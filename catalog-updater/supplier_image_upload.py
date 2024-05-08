#!/usr/bin/env python3

import requests
import os
from PIL import Image


url = 'http://localhost/upload/'

img_path = 'supplier-data/images/'

for files in os.listdir(img_path):
    if files.endswith('jpeg'):
        with open(img_path + '/' + files, 'rb') as pics:
            r = requests.post(url, files={'file': pics})