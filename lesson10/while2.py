#здачача 1(вывод суммы)
print("S=1+2+3+4+...+n")
n=int(input("Ведите конечное значение суммы n"))

s=0
i=1
while i<=n:
    s+=i  
    i+=1   
print(s)
#здачача 1(вывод факториала)
n=int(input("Введите значение факториала"))

s=1
i=1
while i<=n:
    s*=i
    i+=1
print(s)
#здачача 1(вывод факториала)
n=int(input("Введите значение n"))

s=0
i=1
a=1/2
while i<=n:
    s+=a
    i+=1
    a/=2
    print(s)
print(s)
#здачача 1(вывод колличество цифр в числе )
n=int(input("Введите  n   ")) 

i=0
while n>0:
    n//=10
    i+=1
  
print(i)
