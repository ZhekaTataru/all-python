spisok=[1,2,3]
spisok_1=[4,5,6]
spisok_global=[(i,x) for i in spisok for x in spisok_1]
#for i in spisok:
#    for x in spisok_1:
#        spisok_global.append((i,x))
print(spisok_global)
for a in spisok_global:
    print(a)
