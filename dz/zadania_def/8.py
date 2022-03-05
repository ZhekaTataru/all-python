a=float(input("Введите сторону а: "))
b=float(input("Введите сторону b: "))
c=float(input("Введите сторону c: "))
def treygolnik():
    if (a>0 and b>0 and c>0)and a+b>c and a+c>b and b+c>a:
        print("Треугольник существует  ")

    else:
        print("Треугольник не существует  ")
treygolnik()    
