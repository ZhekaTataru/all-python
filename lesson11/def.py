def summa(a_1, b_1):  # a, b - входные параметры
    global c            # глобальная переменная
    c = a_1+b_1


a = int(input("Введите первое число ---> "))
b = int(input("Введите второе число ---> "))
summa(a, b)
print(c)
