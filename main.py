#!/usr/bin/env python3

import shutil
from datetime import date
import smtplib
import os

#Get variables
EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

#Trying To Backup
def backup_folder():
    try:
        today = date.today()
        today_format = today.strftime(f"%m-%d-%y")
        SRC = "C:\\Users\\PeanutTheAdmin\\Documents\\Python Projects"
        DST = f"\\\\192.168.1.254\\Shared\\Projects\\PythonBackup\\{today_format}"
        shutil.copytree(SRC, DST)
        status = "Success"
        return status
    except:
        status = "Fail"
        return status

#Send Backup Status
def send_email(status):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = "Python Projects Backup Status"
        body = status

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(EMAIL_ADDRESS, "recipient.email.here@jacobcavaness.com", msg)

status = backup_folder()
send_email(status)
