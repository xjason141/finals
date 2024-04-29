#send email message using smtplib
import smtplib
import getpass
from email.message import EmailMessage

msg = EmailMessage()

sender = 'hamdi.zecl@gmail.com'
recipient = 'dodo@gmail.com'

#'from', 'to' and 'subject' are examples of email header fields.
#They’re key-value pairs of labels and instructions used by email clients and servers to route and display the email.
msg['From'] = sender
msg['To'] = recipient

#setting up email server
mail_server = smtplib.SMTP_SSL('smtp.example.com') #this address produces 'socket.gaierror: [Errno 11001] getaddrinfo failed'
mailPass = getpass.getpass('Password? ') #authenticate to the server
# print(mailPass)

mail_server.login(sender, mailPass)

mail_server.send_message(msg) #should return and empty dict if message is successfully sent

mail_server.quit()

