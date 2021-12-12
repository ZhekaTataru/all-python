#Подпрограммы
def site():
    while mass1:
        c1=mass1.pop(0)
        print(f"Сайт {c1} в разработке")
        mass2.append(c1)

def complete():
    for el in mass2:
        print(f"{el} готов")

#основной код
mass1=["Сайт1","Сайт2","Сайт3","Сайт4"]
mass2=[]
site()
complete()
