#!/usr/bin/env python3

import mimetypes
import os
from email.message import EmailMessage
import smtplib

def generate_email(sender, recipient, title, content):
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Title'] = title
    msg.set_content(content)
    
    return msg

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
