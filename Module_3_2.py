
def send_email(message, recepient, *, sender = "university.help@gmail.com"):
    if "@" in recepient and "@" in sender:
        if sender.endswith('.com') or sender.endswith(".ru") or sender.endswith(".net"):
            if recepient.endswith(".com") or recepient.endswith(".ru") or recepient.endswith(".net"):
                if recepient == sender:
                    print("Нельзя отправить письмо самому себе!")
                elif sender != "university.help@gmail.com" :
                    print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса",sender ,"на адрес", recepient)
                else:
                    print("Письмо успешно отправлено с адреса", sender, "на адрес", recepient)
            else:
                print("Невозможно отправить письмо с адреса", sender, "на адрес", recepient)
        else:
            print("Невозможно отправить письмо с адреса", sender, "на адрес", recepient)
    else:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recepient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')