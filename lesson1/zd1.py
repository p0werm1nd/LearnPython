#Домашнее задание №1
#Условный оператор: Возраст
#* Попросить пользователя ввести возраст при помощи input и положить  результат в переменную
#* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
#  учиться в детском саду, школе, ВУЗе или работать
#* Вызвать функцию, передав ей возраст пользователя и положить результат
#  работы функции в переменную
#* Вывести содержимое переменной на экран

def life(age):
    age = int(age)
    if 3 < age < 6:
        result = 'Ты должен ходить в детский сад'
    elif 6 <= age <= 17:
        result = 'Ты должен ходить в школу'
    elif 18 <= age <= 24:
        result = 'Ты должен ходить в ВУЗ'
    elif 24 < age < 60:
        result = 'Ты должен ходить на работу'
    else:
        result = 'Ты никому ничего не должен'
    return result

def main():
    age = input('Вееди свой возраст и нажми Enter')
    youmust = life(age)
    print(youmust)
    return

if __name__ == "__main__":
    main()
