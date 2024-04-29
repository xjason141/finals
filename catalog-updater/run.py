#! /usr/bin/env python3

import os
import requests

txt_path = 'catalog-updater/supplier-data/descriptions/001.txt'

texts_path = 'catalog-updater/supplier-data/descriptions/'

fin = {}
for files in os.listdir(texts_path):
    k = ['name', 'weight', 'description', 'image_name']
    count = 0
    fin = {}
    with open(texts_path + files) as desc:
        for lines in desc:
            if ' lbs' in lines:
                weight = int(lines[:-4].strip())
                fin[k[count]] = weight
            else:
                fin[k[count]] = lines.strip()
            count += 1

    print(fin)


