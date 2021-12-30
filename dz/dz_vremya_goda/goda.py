def month_seasons(n,value):
    for z,x in month.items():
        if n in z:
            value=x
            break
        elif n>12 and n<1:
            print(none)
            break 
    return value

month={
    (12,1,2):"winter",
    (3,4,5):"spring",
    (6,7,8):"summer",
    (9,10,11):"autumn"
    }
none=f"error"
About=int(input("ведите номер месяца : "))

print(month_seasons(About,none))
