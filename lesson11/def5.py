def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

name = input("Name --> " )
l_name = input("Last name --> ")
musician = get_formatted_name(name, l_name)
print(musician)
