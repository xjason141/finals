#simple email message
import mimetypes
import os
from email.message import EmailMessage

msg = EmailMessage()

sender = 'didi@gmail.com'
recipient = 'dodo@gmail.com'

#'from', 'to' and 'subject' are examples of email header fields.
#They’re key-value pairs of labels and instructions used by email clients and servers to route and display the email.
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = f'Greetings from {sender} to {recipient}'

body = '''Hey you!
I'm currently learning how to setup email in python.'''

msg.set_content(body)

#prepping attachment for email
att_path = 'emails\emailing\kaala.png'
file_path = os.path.basename(att_path)
file_type, _ = mimetypes.guess_type(file_path)

#mime_type string contains the MIME type and subtype, separated by a slash.
#The EmailMessage type needs a MIME type and subtypes as separate strings, so let's split this up:
stype, ssubtype = file_type.split('/') 

with open(att_path, 'rb') as ap:
    msg.add_attachment(ap.read(),
                       maintype=stype,
                       subtype=ssubtype,
                       filename=os.path.basename(att_path)
                       )
print(msg)