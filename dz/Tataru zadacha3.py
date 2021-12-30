import math
x=float(input("Введите x --> "))
if x<2 and x>=0:
    y=x*(math.sqrt(math.fabs(x+5.4)))
    print(y)
elif x<8 and x>=2:
    y=(math.atan(x)*math.atan(x))
    print(y)
elif x>=8:
    y=math.log10(math.fabs(x-7.8))
    print(y) 
