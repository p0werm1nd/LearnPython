#Домашнее задание №1
#Цикл for: Оценки
#* Создать список из словарей с оценками учеников разных классов
#  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#* Посчитать и вывести средний балл по всей школе.
#* Посчитать и вывести средний балл по каждому классу.

def main():

    classy_ocenki = [{'class': '1a', 'ocenki': [3, 4, 4, 3]},
                     {'class': '2a', 'ocenki': [5, 4, 3, 4, 5]},
                     {'class': '2b', 'ocenki': [5, 5, 5, 5, 5, 5]},
                     {'class': '3a', 'ocenki': [4, 4, 4, 4, 4]},
                     {'class': '3b', 'ocenki': [3, 3, 3, 3]},
                     {'class': '3v', 'ocenki': [3, 5, 3, 5, 3]}]

    vse_ocenki = []
    for class_ocenki in classy_ocenki:
        vse_ocenki = vse_ocenki + class_ocenki['ocenki']
#для дебага
#    print(vse_ocenki)
    print('Средний балл по оценкам =', sum(vse_ocenki) / len(vse_ocenki))

    for kagdyj_class in classy_ocenki:
#        print (kagdyj_class)
        print('Средний балл в классе ', kagdyj_class['class'], ' = ', sum(kagdyj_class['ocenki']) / len(kagdyj_class['ocenki']))
    return

if __name__ == "__main__":
    main()
