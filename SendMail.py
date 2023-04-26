import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Адрес отправителя и получателя
sender_email = "отправитель@mail.ru"
receiver_email = "получаель@mail.ru"

# Настройка заголовков письма
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Тема письмеца"

# Текст сообщения
message = "привет!"

# Создание объекта MIMEText и добавление его к сообщению
msg_body = MIMEText(message, 'plain')
msg.attach(msg_body)

# Подключение к SMTP-серверу и отправка письма
with smtplib.SMTP_SSL('smtp.mail.ru', 465) as server:
    server.login(sender_email, 'пароль(для внешних приложений)')
    server.sendmail(sender_email, receiver_email, msg.as_string())