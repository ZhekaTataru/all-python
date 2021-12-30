import random
#a=[2,3,45,71,435,67789,8]
#f=list( map(lambda x:x**2,a))
#print(f)
"""zadacha"""
#a=[random.randint(0,10) for i in range(11)]
#f=list( map(lambda x:x**3,a))
#print(f)
def f(i):
    if i%2==0:
        return True
    else: return False

    


    
a=[random.randint(0,15) for i in range(10)]
y=list(filter(f,a))
print(y)
