def string_comparison(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        result = 0
    elif str1 == str2:
        result = 1
    elif len(str1) > len(str2):
#По заданию непонятно нужно ли возвращать обы числа - 2 и 3 если оба условия выполняются =/
#Поэтому сделал взаимоисключение что бы не было ошибок понимания при интерпретации результата
        if str2 == 'learn':
            result = 3
        else:
            result = 2
    else:
        result = 42
#Вариант 42 нужен что бы не было ошибок понимания при интерпретации результата
    return result


def main():
    print(string_comparison('вариант первый', 1234))
    print(string_comparison('вариант равенства', 'вариант равенства'))
    print(string_comparison('первая строка длиннее чем', 'вторая'))
    print(string_comparison('имеем спеслово', 'learn'))
    print(string_comparison('=/', 'learn'))
    
if __name__ == "__main__":
    main()
