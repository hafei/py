# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 21:32:00 2018

@author: Sean
"""

import socks
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import COMMASPACE


gmail_user = 'zhangmeng@gmail.com'
gmail_password = 'zhangmeng'
user_account = {'username':gmail_user,'password':gmail_password}
SOCKS5_PROXY_HOST = '127.0.0.1'
SOCKS5_PROXY_PORT = 2080

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, SOCKS5_PROXY_HOST,SOCKS5_PROXY_PORT)
socks.wrapmodule(smtplib)

# email message
send_from = 'zhangmengcoding@gmail.com'  
to = ['zhangmengcoding@gmail.com','zhangmengcoding@hotmail.com']  
subject = 'OMG Super Important Message'  
body = 'Hey, what\'s up?\n\n- You'

# gmail smtp server
smtp_host = 'smtp.gmail.com'
smtp_port = 587

def send_mail(receivers,text,sender=send_from,user_account = user_account,subject=subject):
    msg_root = MIMEMultipart()
    msg_root['Subject'] = subject
    msg_root['To'] = COMMASPACE.join(receivers)
    msg_text = MIMEText(text,'html','utf-8')
    msg_root.attach(msg_text)
    
    smtp =  smtplib.SMTP(smtp_host,smtp_port)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(gmail_user,gmail_password)
    smtp.sendmail(sender,receivers,msg_root.as_string())
    
send_mail(to,body)    
    


