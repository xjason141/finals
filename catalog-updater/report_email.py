#!/usr/bin/env python3

import os
import datetime
import reports
import emails

date = datetime.datetime.now().strftime('%d-%B-%Y')

desc_dir = 'catalog-updater/supplier-data/descriptions/'
# desc_files = os.listdir(desc_dir)


def generate_pdf():
    blank = ''
    pdf_report = ''
    for files in os.listdir(desc_dir):
        if files.endswith('txt'):
            with open(desc_dir + files, 'r') as file:
                lines = file.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                
                pdf_report += 'name: ' + name + '<br/>' + 'weight: ' + weight + '<br/><br/>'
        # print(pdf_report)
    # return pdf_report
    print(pdf_report)


if __name__ == '__main__':
    title = 'PDF generated on ' + date
    data = generate_pdf(desc_dir)
    reports.generate_report('/tmp/processed.pdf', title, data)


sender = 'automation@example.com'
recipient = 'student@example.com'
title = 'Upload Completed - Online Fruit Store'
content = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
atth_path = '/tmp/processed.pdf'

message = emails.generate_email(sender, recipient, title, content, atth_path)
emails.send_email(message)

generate_pdf()