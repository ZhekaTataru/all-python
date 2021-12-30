print(3.4)
guest=["bogdan", "egor", "danya"]
print(guest)
a=f"{guest[0].title()} приглашаю тебя на обед!"
print(a)
b=f"{guest[1].title()} приглашаю тебя на обед!"
print(b)
c=f"{guest[2].title()} приглашаю тебя на обед!"
print(c)
print(3.5)
x=f"{guest[0].title()}: Я не смогу прийти."
print(x)
guest[0]="den"
print(guest)
z=f"{guest[0].title()} приглашаю тебя на обед!"
print(z)
b=f"{guest[1].title()} приглашаю тебя на обед!"
print(b)
c=f"{guest[2].title()} приглашаю тебя на обед!"
print(c)
print(3.6)
print("Список гостей можно расширить!")
guest.insert(0,"vova")
guest.insert(3,"zheka")
guest.append("vlad")
print(guest)
print(3.7)
print("К сожелению на обед могут прийти только два гостя(")
v=f"{guest[5].title()} прости, я сожалею о отмене приглашения!"
guest.pop(5)
print(v)
print(guest)
n=f"{guest[3].title()} прости, я сожалею о отмене приглашения!"
print(n)
guest.pop(3)
print(guest)
m=f"{guest[0].title()} прости, я сожалею о отмене приглашения!"
guest.pop(0)
print(m)
print(guest)
s=f"{guest[2].title()} прости, я сожалею о отмене приглашения!"
guest.pop(2)
print(s)
print(guest)
g=f"{guest[0].title()} приглашение остается в силе!"
print(g)
f=f"{guest[1].title()} приглашение остается в силе!"
print(f)
print(guest)
del guest[0]
del guest[0]
print(guest)


