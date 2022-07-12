import smtplib
from email.message import EmailMessage
import shutil
from email.mime.text import MIMEText
import email.utils
from string import Template
from pathlib import Path

html = Template(Path('./index.html').read_text())
email = EmailMessage()
email['from'] = 'Nguyen Luat'
email['to'] = 'nguyenluathcmut@gmail.com'
email['subject'] = 'You won 1,000,000 dollars.'
email.set_content(html.substitute({'name': 'TinTin'}), 'html')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('nguyenluathcmut@gmail.com', 'gohgcumagdouhegk')
    smtp.send_message(email)
    print("Done!")

'''
Step to send mail with attachments using SMTP
- Create MIME
- Add sender, receiver address into MIME
- Add the mail title into the MIME
- Attach the body into the MIME
- Start the SMTP session with valid port number with proper security features
- Login to the system
- Send email and exit
'''