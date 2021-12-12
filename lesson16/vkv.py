users={
    "Zhenya":["task1","task2","task3","task4"], 
    "Sasha":["task1","task2"],
    "Den":["task1"],
    "Vova":["task1","task2","task3","task4","task5","task6"],
    "Vlad":["task1","task2","task3","task4","task5","task6","task7","task8","task9","task10"]
    }

for z,x in users.items():
    print("-"*40)
    print(f"Его зовут {z} , он решил такие задачи : ")
    for task in x:
        print(f"\t\/{task}")
    print("-"*40)
