def menu(sizes,*Bogdan):
    print(f"Вы выбрали такие пиццы, c размером {sizes}:")
    for i in Bogdan:
        print(f"-{i}")
size=input("Введите размер пиццы")
menu(size,"Четыре мяса")
menu(size,"Гаваи","Четыре сыра","Вова")
