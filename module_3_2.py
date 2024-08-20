def send_email(mess, rec, sen="university.help@gmail.com"):

    if "@" in rec and "@" in sen:
        if rec == sen:
            print("Нельзя отправить письмо самому себе!")
        else:
            if sen == "university.help@gmail.com":
                print(f"Письмо успешно отправлено с адреса {sen} на адрес {rec}.")
            else:
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sen} на адрес {rec}.")
    else:
        print(f"Невозможно отправить письмо с адреса {sen} на адрес {rec}")

send_email("123", "vasyok1337@gmail.com")
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sen='urban.info@gmail.com')