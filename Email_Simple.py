# go over to your gmail account and setup 2-factor authentication
# generate app password
# create a function to send the mail

# email library built in python
from email.message import EmailMessage
# library created by me to secure my password to my gmail code written login
from secret_key import passkey
# These library are built in python for security purpose when we work with email
# SSL(secure socket layer) and also known as TLS(transport layer security)
import ssl
import smtplib

# creating email font phase
email_sender = "--------235@gmail.com"
# this is email generated from Google security app
email_password = passkey()

email_receiver = "------235@gmail.com"

subject = "Don't forget to subscribe"

body = """
When you watch a video, please hit subscribe.
Tech with intelligent..
"""
# instant package for EmailMessage
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("Your mail went successfully")
