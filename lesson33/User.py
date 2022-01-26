class User:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        #9.5{
        self.login_attempts=0
        #9.5}
    def describe_user(self):
        print(f"Фамилия:{self.first_name} имя:{self.last_name} возраст:{self.age}")
    def greet_user(self):
        print(f"Приветствую, {self.first_name} {self.last_name}!")
        #9.5{
    def increment_login_attempts(self):
        self.login_attempts+=1
        print(f"Количество попыток входа в аккаунт: {self.login_attempts}")
    def reset_login_attempts(self):
        self.login_attempts*=0
        print(f"Количество попыток входа в аккаунт: {self.login_attempts}")
        #9.5}
