import os
import smtplib
from segredos import senha
from email.message import EmailMessage

#configurar email senha
EMAIL_ADDRESS = 'email de quem envia'
EMAIL_PASSWORD = senha

#criar email
msg=EmailMessage()
msg['Subject']='texto'
msg['from']='email de quem envia'
msg['to']='email de quem recebe'
msg.set_content('arquivo de mensagem')

#enviar email
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
