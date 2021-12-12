def gen():
    x=2
    print("perviy perebor")
    yield x
    x*=2
    print("vtoroy perebor")
    yield x
    x/=2
    print("tretiy perebor")
      
t=gen()
for i in gen():
    print(i)




