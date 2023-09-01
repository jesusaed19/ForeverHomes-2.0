import smtplib 
from email.message import EmailMessage
from config import PASSW

def email(mail, name, project):
    email_subject = name
    sender_email_address = "contactforeverhomes@gmail.com"
    receiver_email_address = "jesusarmandoed57@gmail.com"
    email_smtp = "smtp.gmail.com"
    email_password = PASSW
    
    
    # create an email messages object
    message = EmailMessage()
    
    # configure email headers
    message['Subject'] = email_subject
    message['From'] = sender_email_address
    message['To'] = receiver_email_address
    
    # set email body text
    
    message.set_content("EMAIL:  " +  mail + "\n \n" + "PROJECT:  " + project)
    
    # set smtp server an port 
    server = smtplib.SMTP(email_smtp, '587')
    
    # identify this client to the SMTP server 
    server.ehlo()
    
    # Secure th SMTP connection 
    server.starttls()
    
    # Login to email account 
    server.login(sender_email_address, email_password)
    
    # send email 
    server.send_message(message)
    
    # close connection to sever 
    server.quit()
    