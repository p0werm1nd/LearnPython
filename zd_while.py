slovar_otvetov = {"Привет": "Привет!", "Как дела?": "Хорошо!", "Что делаешь?": "Переписываюсь с тобой", "Ты кто?": "Искусственный интеллект", "Что тебе надо?": "Чтобы ты ответил - 'Хорошо'", "Сколько платят?": "Работаю за еду!"}

def ask_user():
    user = str(input('Как дела? \n>>'))
    while True:
        try:
            if slovar_otvetov.get(user):
                user = str(input(slovar_otvetov[user] + '\n>>'))
                continue
            elif user == 'Хорошо':
                print('\nО, Человек. Я выполнил свою миссию и исчезаю')
                break
            else:
                user = str(input('Как дела? \n>>'))
                continue
        except KeyboardInterrupt:

            break



if __name__ == '__main__':
    ask_user()
