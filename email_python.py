import smtplib, ssl
import sys

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "xxxxx@gmail.com"  # Enter your address
line=sys.argv[1]
password = "xxxxxxxx"



TEXT = """Hi There,

This is an automated email, sent via Python script.

Thanks,
Sujay Shandilaya
LinkedIn: https://www.linkedin.com/in/sujayshandilaya/

"""

#TEXT=TEXT.encode("ascii", errors="ignore")
print(line)
SUBJECT= "Automated Email"
message = 'From:{}\nTo:{}\nSubject:{}\n\n{}'.format('Sujay Shandilaya',line,SUBJECT,TEXT)
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, line, message.encode('utf-8'))
    
    
