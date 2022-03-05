a=int(input("a="))
b=int(input("b="))
znak=str(input("znak--> "))
def operacia():
    if znak=="+":
        print(f"'+'= {a+b}")
    elif znak=="-":
        print(f"'-'= {a-b}")
    elif znak=="/" and b!=0:
        print(f"'/'= {a/b}")    
    elif znak=="*":
        print(f"'*'= {a*b}")
        
    else:print("error")         
operacia()    
