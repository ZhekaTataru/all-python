import math
x=float(input("Введите x --> "))
if math.fabs(x)<2:
    y= x-math.exp(x)
    print(y)
elif x<=(-2):
    y=math.log10(x*x)
    print(y)
elif x>=2:
    y=math.sin(x)* math.sin(x)
    print(y) 
