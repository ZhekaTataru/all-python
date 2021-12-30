import math
x=float(input("Введите x --> "))
if x>1 and x<3.2:
    y=-((1.4+x)/math.log(x))
    print(y)
elif x>0 and x<=1:
    y=(x**2)-0.75
    print(y)
elif x<=0:
    y=math.pow(math.cos(x*x),3)- math.pow(math.sin(x*x),3)
    print(y)
