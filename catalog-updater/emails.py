#!/usr/bin/env python3

import mimetypes
import os
from email.message import EmailMessage
import smtplib

def generate_email(sender, recipient, title, content, atth_path):
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Title'] = title
    msg.set_content(content)

    file = os.path.basename(atth_path)
    file_type, _ = mimetypes.guess_type(file)
    file_type, f_subtype = file_type.split('/', 1)

    with open(atth_path, 'rb') as ap:
        msg.add_attachment(ap.read(),
                           maintype=file_type,
                           subtype=f_subtype,
                           filename=file)
    
    return msg

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
