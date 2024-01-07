import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

subject = "sending msg"
body = "hi my name is swastik"
sender = "swastikgahukarcr7@gmail.com"
recipients = ["swastik.gahukar.ai@ghrietn.raisoni.net"]
password = "rdlc luht rbou dgrv"

with open("D:\log.pdf", "rb") as attachment:
    # Add the attachment to the message
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename= 'D:\log.pdf'",
)


def send_email(subject, body, sender, recipients, password):
    msg = MIMEMultipart()

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    html_part = MIMEText(body)
    msg.attach(html_part)
    msg.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)