import smtplib
from email.message import EmailMessage

sender_email = 'pythontest1234@yandex.ru'
recipient_mail = 'qqq968@yandex.ru'
password = 'uxezbjsxmdzqbbqp'
subject = 'Проверка связи'
body = 'Hi, from Python!'

msg = EmailMessage()
msg.set_content(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recipient_mail

try:
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.login(sender_email, password)
    server.send_message(msg)
    print('Mail sent!')
except Exception as e:
    print(f'Error - {e}')
finally:
    if server:
        server.quit()
