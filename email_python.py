import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys

smtp_server = "smtp.gmail.com"
port = 465
sender_email = "shandilayasujay@gmail.com"
password = ""
receiver_email = sys.argv[2]
pdf_file = "Shandilaya,Sujay-TX-DataEngineer.pdf"
name=sys.argv[1]
# Create a multipart message
message = MIMEMultipart()
message["From"] = "Sujay Shandilaya"
message["To"] = receiver_email
message["Subject"] = "Passionate Data Engineer in US Seeking Opportunity at Mixpanel || Senior Software Engineer,Growth Infrastructure"

# Add the body text to the message
body = """Hello {},

I am a data engineer with 4+ years in this industry and good hands-on skills in SQL,Bigquery,Python, ETL data pipelines, and past experience working in the startup environment. I am interested in working full-time at Mixpanel because of my interest in developing strategic data pipelines to bring data that can solve business problems.

Could you please help me get started with the interview process?

Regards,
Sujay Shandilaya
Direct: +1 4699274787
""".format(name)


message.attach(MIMEText(body, "plain"))

# Add the PDF attachment to the message
with open(pdf_file, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {pdf_file}",
)
message.attach(part)

# Create an SSL context and connect to the SMTP server
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.send_message(message)
