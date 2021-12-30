import math
x=float(input("Введите x --> "))
y=float(input("Введите y --> "))
if x<0 and math.fabs(x*y)<1:
    z=(x+y)/math.exp(x*y)
    print(z)
elif x>2 and y<=0:
    z=(-math.log(x))* math.log(x)
    print(z)
elif x>=0 and x<=2 and y>0:
    z=math.log(math.sqrt(y))
    print(z)    
