import credentials

import smtplib
import imghdr
import os

from email.message import EmailMessage

def send(df):
    msg = EmailMessage()
    msg['Subject'] = 'STOCK UPDATE'
    msg['From'] = credentials.EMAIL_ADRESS
    msg['To'] = credentials.EMAIL_ADRESS
    msg.set_content('The following stock has either reached an emotional or rational barrier. Analyse for further action:')
    msg.add_alternative(df, subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(credentials.EMAIL_ADRESS, credentials.EMAIL_PASSWORD)    
        smtp.send_message(msg)
        print('ERFOLGREICH VERSENDET')

