def menu(*sendvich):
    print(f"Вы выбрали такие ингредиенты: {ingredient}")
    for i in sendvich:
        print(f"-{i}")
ingredient=input("Введите желаимые ингредиенты:")
menu(ingredient)
