import math
a=int(input("x="))
h=int(input("h="))
d=int(input("d="))
s = 0.5*a*h
p=(a+h+d)/2
Sr=float(math.sqrt(p*(p-a)*(p-h)*(p-d)))
print(p)
print(Sr)
