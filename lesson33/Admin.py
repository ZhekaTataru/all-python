from User import *
#9.7
class Admin(User):
    def __init__(self,first_name,last_name,age):
        User.__init__(self,first_name,last_name,age)
        self.privileges=["Allowed to delete users","Allowed to add message", "Allowed to ban users"]
    def greet_admin(self):
        print(f"Приветствую администрацию, {self.first_name} {self.last_name}!")    
    def show_privileges(self):
        print("Привилегии админа:")
        for i in self.privileges:
            print(i)
#9.8
class Privileges(Admin):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges=["Allowed to delete users","Allowed to add message", "Allowed to ban users"]            
