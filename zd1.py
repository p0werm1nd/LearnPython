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
