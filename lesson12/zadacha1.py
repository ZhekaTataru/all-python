klient=["Сайт1","Сайт2","Сайт3","Сайт4"]
mykompany=[]

while klient:
    c1=klient.pop(0)
    print(f"Сайт {c1} в разработке")
    mykompany.append(c1)
for el in mykompany:
    print(f"{el} готов")
print(mykompany)
