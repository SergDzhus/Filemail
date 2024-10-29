import smtplib
from email.message import EmailMessage
from email.utils import parseaddr
from tkinter import *


def validate_email(email):
    name, addr = parseaddr(email)
    return '@' in addr and '.' in addr.split('@')[-1]


def save():
    with open('save.txt', 'w') as file:
        file.write(sender_email_entry.get() + '\n')
        file.write(recipient_email_entry.get() + '\n')
        file.write(password_entry.get() + '\n')


def load():
    try:
        with open('save.txt', 'r') as file:
            info = file.readlines()
            sender_email_entry.insert(0, info[0].strip())
            recipient_email_entry.insert(0, info[1].strip())
            password_entry.insert(0, info[2].strip())
    except FileNotFoundError:
        pass


def send_email():
    save()
    sender_email = sender_email_entry.get()
    recipient_email = recipient_email_entry.get()

    if not validate_email(sender_email) or not validate_email(recipient_email):
        result_label .config(text='Ошибка, неверный формат e-mail!')
        return

    password = password_entry.get()
    subject = subject_entry.get()
    body = body_text.get(1.0, END)

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    server = None

    try:
        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        server.login(sender_email, password)
        server.send_message(msg)
        result_label.config(text='Mail sent!')
    except Exception as e:
        result_label.config(text=f'Error - {e}')
    finally:
        if server:
            server.quit()

window =Tk()
window.title("Отправка e-mail")
window.geometry('500x300')

Label(text='Отправитель:').grid(row=0, column=0, sticky=W)
sender_email_entry = Entry()
sender_email_entry.grid(row=0, column=1, sticky=W)

Label(text='Получатель:').grid(row=1, column=0, sticky=W)
recipient_email_entry = Entry()
recipient_email_entry.grid(row=1, column=1, sticky=W)

Label(text='Пароль приложения:').grid(row=2, column=0, sticky=W)
password_entry = Entry()
password_entry.grid(row=2, column=1, sticky=W)

Label(text='Тема письма:').grid(row=3, column=0, sticky=W)
subject_entry = Entry()
subject_entry.grid(row=3, column=1, sticky=W)

Label(text='Текст письма:').grid(row=4, column=0, sticky=W)
body_text = Text(width=45, height=10)
body_text.grid(row=4, column=1, sticky=W)

Button(text="Отправить!", command=send_email).grid(row=5, column=1, sticky=W)

result_label = Label(text='')
result_label.grid(row=6, column=1, sticky=W)

load()

window.mainloop()
