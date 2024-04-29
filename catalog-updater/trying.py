import os

texts_path = 'catalog-updater/supplier-data/descriptions/'

for files in os.listdir(texts_path):
    with open(texts_path + files) as files:
        for lines in files:
            if ' lbs' in lines:
                x = int(lines[:-4])
                print(type(x))
            else:
                print(lines.strip())
