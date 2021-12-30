import math
#zadacha1
#print("zadacha1")
#r=int(input("Введите радиус круга --> "))
#if r>0:
#    d=r+r
#    print(f"Диаметр круга равен {d}")
#    l=math.pi*d
#    print(f"Длина круга равна {int(l)}")
#    s=math.pi*(r**2)
#    print(f"Площадь круга равна {int(s)}")
#else:
#    print("Радиус должен быть больше 0!")    
#print("--------------------")
#zadacha2
#print("zadacha2")
#p=("aba12345")
#print(f"Правильный пароль--> {p}")
#vhod=input("Введите пароль для входа: ")
#if(vhod==p):
#    print("Вход разрешен. Добро пожаловать!")
#else:
#    print("Вход заблокирован. Неверный парооль!")
#print("--------------------")
#zadacha3
#print("zadacha3")
#age=int(input("Введите свой возраст--> "))
#min_zp=int(input("Введите суму вашего дохода(в гривнах)--> "))
#if age>=18 and min_zp>=5000:
#    print("Вы можете взять кредит.")
#else:
#    print("Вы  не можете взять кредит.")
#print("--------------------")
#zadacha4
#print("zadacha4")
#bal=int(input("Введите количество баллов( от 0 до 100)--> "))
#if bal<=100 and bal>=0:
#        if bal>= 90:
#            print("Ваша оценка А!")
#        elif bal >= 80:
#            print("Ваша оценка B!")
#        elif bal >= 70:
#            print("Ваша оценка C!")
#        elif bal >= 60:
#            print("Ваша оценка D!")
#        else:
#            print("У вас незачет!!!")
#else:
#    print("Количество балов должно быть в диапазоне от 0 до 100!")
#print("--------------------")
#zadacha5
#print("zadacha5")
#x=int(input("Введите Х --> "))
#y=int(input("Введите У --> "))
#if x>y:
#    z=math.sqrt(x*y)
#    print(z)
#else:
#    z=math.log(x+y)
#    print(z)
#print("--------------------")
 #zadacha6   
#print("zadacha6")
#t=int(input("Введите емпературу в комнате --> "))
#if t>20:
#    print("on")
#else:
#    print("off")
#print("--------------------")
 #zadacha7 
#print("zadacha7")
#n=int(input("Введите номер --> "))
#print(f"Вася стоит {n} по счету")
#if n%2==0:
#    print("Второй")
#else:print("Первый")    
#print("--------------------")
 #zadacha8 
#print("zadacha8")
#x=int(input("Введите сторону x --> "))
#y=int(input("Введите сторону y --> "))
#z=int(input("Введите сторону z --> "))
#if (x+y)>z or (x+z)>y or (z+y)>x:
#    print("Теугольник существует")
#else: print("Теугольника нету")    
#print("--------------------")
 #zadacha9 
#print("zadacha9")
#x=int(input("Введите координату x --> "))
#y=int(input("Введите координату y --> "))
#print(f"Точка с координатами ({x},{y})")
#if x>0 and y>0:
#    print("Точка принадлежит первой четверти")
#elif x<0 and y<0:
#    print("Точка принадлежит третьей четверти")
#elif x<0 and y>0:   
#    print("Точка принадлежит второй четверти")
#elif x>0 and y<0:   
#    print("Точка принадлежит четвертой четверти")
#elif x==0 and y==0:
#    print("Центр координат")    
#else: print()
#print("--------------------")
 #zadacha10 
#print("zadacha10")
x=int(input("Введите x --> "))
if x>0:
    y=(2*x)-10
elif x==0:
    y=0   
else:
    y=(2*math.fabs(x))-1
print(f"y={y}")    
