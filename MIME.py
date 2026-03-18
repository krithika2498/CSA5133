from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender_email = input("Enter sender email: ")
receiver_email = input("Enter receiver email: ")
subject = input("Enter subject: ")
body = input("Enter email body: ")
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

print("\nMIME Email Content:\n")
print(msg.as_string())
