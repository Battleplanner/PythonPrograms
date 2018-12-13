#This was only made possible due to this video: https://youtu.be/YPiHBtddefI

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#If you want to send attachments, the following modules are also necessary
from email.mime.base import MIMEBase
from email import encoders
import os.path

email = "mirak.ictman@gmail.com"
password = "MK-110631"
send_to_email = "shaimaa_yaseen@hotmail.com"
subject = "You recieved an email from some code!"
message = "This is an email sent by a few lines of Python code as a test for some of my projects."

msg = MIMEMultipart()
msg["From"] = email
msg["To"] = send_to_email
msg["Subject"] = subject
folder_location = "C:\\Users\\mirak\\Desktop\\logs" #This gives the location of the file you want to send

msg.attach(MIMEMultipart(message, "plain"))
foldername = os.path.basename(folder_location) #This will be the filename displayed to the recipient of the email
attachment = open(folder_location, "rb") #Opens the file using read binary
part = MIMEBase("application", "octet-stream") #Creates a MIMEBase Object called part passing application and octet-stream as arguments
part.set_payload((attachment).read()) #Passes the contents of the file we just opened
encoders.encode_base64(part) #And then encode the contents using base64
part.add_header("Content-Disposition", "attachment; filename= %s" % foldername) #Adds a header called Content Disposition, declaring it as an attachment and providing the filename

msg.attach(part) #Attaches the attachment to the email

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()

