import math
a = int(input("Введите число"))
if a>0:
    x = math.sqrt(a)
    print(x)
    x = math.sqrt(a), math.sqrt(a)*(-1)
    print(x)
elif a==0:
    print(0)
else:
    print(error)
print(a)
