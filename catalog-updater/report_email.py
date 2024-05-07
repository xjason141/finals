#!/usr/bin/env python3

import os
import datetime
import reports

date = datetime.datetime.now().strftime('%d-%B-%Y')

desc_dir = 'catalog-updater/supplier-data/descriptions/'
desc_files = os.listdir(desc_dir)


def generate_pdf(filepath):
    blank = ''
    pdf_report = ''
    for files in desc_files:
        if files.endswith('txt'):
            with open(filepath + files, 'r') as file:
                lines = file.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                
                pdf_report += f'{blank}\n name: {name}\n weight: {weight}\n{blank}'
        # print(pdf_report)
    return pdf_report


if __name__ == '__main__':
    title = 'PDF generated on ' + date
    data = generate_pdf(desc_dir)
    reports.generate_report('/tmp.processed.pdf', title, data)
