def a():
    b=2
    d=b*b
    yield d
    print("privet")
    yield b
x=a()
print(next(x))
print(next(x))
