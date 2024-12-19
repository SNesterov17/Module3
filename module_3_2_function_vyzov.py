def send_email(message, recipient,*, sender = "university.help@gmail.com"):
    while 1 > 0:
        if "@" not in recipient or "@" not in sender:
            print('Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru')
            break
        if recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net')):
            break
        else:
            print('Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru')
            break
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    if sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com')
    if sender == "urban.info@gmail.com":
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')