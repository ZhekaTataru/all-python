import math
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print(a,"x^2","+",b,"x" "+",c,"=0")
d=b*b-4*a*c
if d>0:
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b-math.sqrt(d))/2*a
    print(int(x1))
    print(int(x2))
elif d==0:
         print(-b/2*a)
else:
    print("error")
         

