#!/usr/bin/env python3
"""
Main script for annims the birthday reminder tool
"""
import smtplib
import account_info as acc
import checkbday as check

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


birthdaystring = "" 
send_email = False

parsed_bdays = check.parse_list()
if len(parsed_bdays) > 0:
    birthdaystring = parsed_bdays
    send_email = True

if send_email:
    msg = MIMEMultipart()
    msg['From'] = acc.my_mail
    msg['To'] = ", ".join(acc.to_mail)
    msg['Subject'] = "Alert! A Birthday is Near!"
    body = "annims has found the following birthday(s) in the near future: \r\n\r\n"                + birthdaystring
    msg.attach(MIMEText(body, 'plain'))

    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(acc.my_mail, acc.password)
    text = msg.as_string()

    smtp_server.sendmail(acc.my_mail, acc.to_mail, text)

