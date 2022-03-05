about=int(input("ведите номер месяца : "))
month={
    (12,1,2):"winter",
    (3,4,5):"spring",
    (6,7,8):"summer",
    (9,10,11):"autumn"
    }
def month_seasons(n,value):
    for z,x in month.items():
        if n in z:
            value=x
            break
        elif n>12 and n<1:
            print(b)
            break 
    return value

b="error"


print(month_seasons(about,b))
