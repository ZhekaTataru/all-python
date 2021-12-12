def gen():
    a=1
    while True:
        if a>1:
            for j in range(2,a):
                if a%j==0:
                    break
                else:
                    yield a
        a+=1
for i in gen():
    print(i)
