def describe_city(city, country):
    print(f"{city} находится в {country}")
    for i in city:
        print(f"")
city=input("Введите название города: ")
describe_city(city, "Украина")

