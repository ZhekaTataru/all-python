import math
x=float(input("Введите x --> "))
if x>(-math.pi)and x<(math.pi/4):
    y=(-math.cos(x-math.pi)*math.cos(x-math.pi))
    print(y)
elif x>(math.pi/4)and x<=1:
    y=math.sqrt(math.fabs(x+1))
    print(y)
elif x>1:
    y=1/(x-1)
    print(y)    
