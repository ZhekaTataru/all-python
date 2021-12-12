a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
D=b*b-4*a*c
if D>0:
    x1 = math.sqrt(-b+D/2*a)
    x2 = math.sqrt(-b-D/2*a)
    print("")
elif D==0:
    x1 = -b/2*a
    print("x =")
else:
        print("error")
