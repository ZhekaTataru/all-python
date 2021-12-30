def make_short(size,text):
    print(f"Вы выбрали футболку, c размером {size} и текстом: {text}")
    for i in text:
        print(f"")
size=input("Введите размер футболки: ")
text=input("Введите желаемый текст на футболке: ")
make_short(size, text)
