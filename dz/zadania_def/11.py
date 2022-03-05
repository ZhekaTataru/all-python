str=str(input("Введите слово: "))
teg=input("Введите teg(<a>,<b>,<img>,<p>): ")
def tegs():
    if teg=="<a>":
        print(f"<a href='URL'>{str}</a>")
    elif teg=="<b>":
        print(f"<b>{str}</b>")
    elif teg=="<img>":
        print(f"<img src='URL' alt='{str}'>")
    elif teg=="<p>":
        print(f"<p>{str}</p>")    
    else:
        print("error")
        
tegs()
