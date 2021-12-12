def greet_user(username, userlast):
    print(f"Hello, {username.title()} {userlast.title()}!")

name = input("Name --> ")
l_name = input("Last name --> ")
greet_user(name, l_name)
