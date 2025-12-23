#  Python Email Sender with Attachment
A Python-based application that sends emails with file attachements using 'Gmail SMTP'.
This project demonstrates how to automate email sending securely using Python's built-in libraries.

# Features
-> Send plain text emails using Python.
-> Attach files (PDF,DOCX,images etc).
-> Secure authentication using 'Gmail App Password'.
-> Uses SMTP with TLS encryption.
-> Beginner-friendly and easy to extend.

# Technologies used
- Python3
- smtplib
- email.mime
- email.encoders
- Gmail SMTP server

# Project structure
|
|---app.py #main python script
|---README.md #project documentation

# Prerequisites
Before running this project , make sure you have:
- Python 3 installed
- A Gmail account
- 'Gmail App Password' enabled

# Enable Gmail App Password
1. Go to Google Account -> Security
2. Enable '2-Step Verification'
3. Generate an 'App Password'
4. Use the generated password in the code

# How to run the project
git clone <paste-repo-link-here>

#after entering the required credentials you will receive a confirmation text which says 'Email sent successfully!'
