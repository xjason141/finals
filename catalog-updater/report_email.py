#!/usr/bin/env python3

import os
from datetime import date
import reports

desc_dir = 'catalog-updater/supplier-data/descriptions/'
desc_files = os.listdir(desc_dir)


def generate_pdf():
    blank = ''
    pdf_report = ''
    for files in desc_files:
        if files.endswith('txt'):
            with open(desc_dir + files, 'r') as file:
                lines = file.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                
                pdf_report += f'{blank}\n name: {name}\n weight: {weight}\n{blank}'
        # print(pdf_report)
    return pdf_report

