#importing necessary libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

#email configuration
sender = input('Enter sender email address:')
receiver = input('Enter receiver email address:')
password = input('Enter sender email password:') #rcpm tvrz jkjg wmvp

#creating  the email content
subject = input('Enter the subject of the email:')
body = input('Enter the body of the email:')

#creating MIMEMultipart object
msg = MIMEMultipart()

msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject
msg.attach(MIMEText(body,'plain')) #converting the body to MIMEText object and attaching it to msg

#attachment path
file_path = input('Enter the file path of the attachment:').strip()  #getting file path from user
file_path = os.path.normpath(file_path) #normalizing the file path

if not os.path.isfile(file_path):
    print("File not found.Please check the path.")
    exit() 
    
#open the file in binary mode
with open(file_path , 'rb') as attachment:
    part = MIMEBase('application','octet-stream') #allows to send any type of file
    part.set_payload(attachment.read()) #reading the file and setting its payload

#encode file to base64
encoders.encode_base64(part)

#add header for attachment
filename = os.path.basename(file_path)
part.add_header(
    'Content-Disposition',
    f'attachment; filename = "{filename}"'
)

#attach the file to email
msg.attach(part)

with smtplib.SMTP('smtp.gmail.com',587) as server:
    server.starttls() #upgrade the connection to a secure encrypted TLS connection
    server.login(sender,password) #log in to your email account
    server.send_message(msg) #send the email
    
print('Email sent successfully!')
