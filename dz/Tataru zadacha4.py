import math
x=float(input("Введите x --> "))
if x>=1:
    y=math.exp(-math.fabs(x))
    print(y)
elif math.fabs(x)<1:
    y=math.log(1-x*x)
    print(y)
elif x<=-1:
    y=math.atan(x)
    print(y) 
