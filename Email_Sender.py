import smtplib # This lib serves as connection between two servers
from email.message import EmailMessage # This is a built-in module for email optimisation.

email = EmailMessage() # This's an obj email
email['From'] = "Ebube Moses" 
email['To'] = "-------235@gmail.com"
email['Subject'] = "My First Email Sender implementation"


email.set_content("I am an intelligent being, just like an ASI optimisation")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: # This server makes transfer email possible.
    smtp.ehlo() # hey smtp is a server saying hello message
    smtp.starttls() # This is an encryption mechanism that keeps our email process securely to the server.
    smtp.login("-------235@gmail.com", "ebubemoses") # This connect the process of the email message.
    smtp.send_message(email)
    print("all good boss!")
    

'''# ^^^ The code on top won't work why because you are to use gmail app password not your real gmail password '''
    
import smtplib
from email.message import EmailMessage
from string import Template # This help to bring placeholder in place of use. e.g: $name >> Ebube by using substitute
from pathlib import Path # This help us to access other or main file paths. e.g: html file or use os.path which is old way to access path.

# These are the receiver gmail address
re_gmail = "mosesebube235@gmail.com"
html = Template(Path("index.html").read_text()) # This is the other file that want to be use(like to be: read or change) in form of Template obj
email = EmailMessage()
email['From'] = "Ebube Moses" 
email['To'] = re_gmail
email['Subject'] = "Your First Email Sender implementation Just Went Boom."
        
email.set_content(html.substitute({"name": "Ebube"}), "html") # This is other file placeholder answer used
    
try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("-------235@gmail.com", "---- put in your generated gmail passkey") # To do, generate gmail app password
        smtp.send_message(email)
        print("Email sent successfully!")
except Exception as e:
    print("An error occurred:", e)
