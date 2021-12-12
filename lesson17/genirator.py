spisok=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
spisok_1=[i if i>5 else "Error" for i in spisok]
#for i in spisok:
#    if i>5:
#        spisok_1.append(i)
#    else:
#       spisok_1.append("Error")
print(spisok_1)
spisok1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
spisok_2=["true_2" if i%2==0 else "true_3" if i%3==0 else "folse" for i in spisok]
#for i in spisok:
#    if i%2==0:
#        spisok_1.append("true_2")
#    elif i%3==0:
#        spisok_1.append("true_3")
#    else:
#        spisok_1.append("folse")
print(spisok_2)
