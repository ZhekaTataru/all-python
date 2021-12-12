a = int(input("Сумма -"))
b = int(input("Ведите процент --->"))
c = int(input("Введите количество месяцев --->"))
if c>12:
    s = a+a*(b/100)
    print(s)
else:
    print(a)
