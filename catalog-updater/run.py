#! /usr/bin/env python3

import os
import requests

texts_path = 'catalog-updater/supplier-data/descriptions/'

for files in os.listdir(texts_path):
    url = 'http://[external-IP-address]/fruits/'
    k = ['name', 'weight', 'description', 'image_name']
    count = 0
    final = {}
    with open(texts_path + files) as desc:
        for lines in desc:
            if ' lbs' in lines:
                weight = int(lines[:-4].strip())
                final[k[count]] = weight
            else:
                final[k[count]] = lines.strip()
            if count == 3:
                final[k[3]] = files.split('.')[0] + '.jpeg'
            count += 1
    
    # r = requests.post(url, json=final)

    # print(r.status_code)
print(final)



