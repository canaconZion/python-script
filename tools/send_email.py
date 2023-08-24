#!/usr/bin/python3
#coding:utf-8
'''
发送邮件
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message):
    # 发送邮箱
    sender_email = ''
    # 邮箱SMTP密钥
    sender_password = ''
    # 接收人邮箱
    recipient_email = '' 
    # 设置SMTP服务器和端口
    smtp_server = 'smtp.163.com'
    smtp_port = 25

    # 创建邮件内容
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(message, 'plain'))

    # 连接SMTP服务器并进行身份验证
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # 发送邮件
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # 关闭连接
    server.quit()

if __name__ == "__main__":
    subject = '编解码消息通知'
    message = '编解码已完成'

    send_email(subject, message)
