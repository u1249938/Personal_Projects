# Author: Ethan Ward
# This script will send an email. Both the login, sender, and recipiet emails 
# need to be filled in (and the password).
#
# Along with the code to send the email, there is also code to read a text file
# and send that as the message, and there is code to attach another file (like
# a text file).

import smtplib
# email specific
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# The first parameter is the provider you want to send through
server = smtplib.SMTP( 'smtp.gmail.com', 587)

# Starts the server
#server.ehlo()
server.starttls()

# Login to account (not recommended to put your password on display)
server.login('iethanward@gmail.com', 'abvrhycxbrugjkjp')

msg = MIMEMultipart()
msg['From'] = 'Ethan'
msg['To'] = 'iethanward@gmail.com'
msg['Subject'] = 'Just a Test'

#with open('message.txt', 'r') as line:
#    message = line.read()

#msg.attach(MIMEText(message, 'plain'))

# To attatch an image:
# filename = 'coding.jpg'
# attachment = open(filename, 'rb') # rb is read bytes

# p = MIMEBase('application', 'octect-stream')
# p.set_payload(attachment.read())

# encoders.encode_base64(p)
# p.add_header('Content-Disposition', f'attachment; filename={filename}')
# msg.attach(p)

#text = msg.as_string()
# sender, target, contents
server.sendmail('iethanward@gmail.com', 'iethanward@gmail.com', 'hello')