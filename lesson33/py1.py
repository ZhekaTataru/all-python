#9.1
from Restaurant  import *
r1=Restaurant("Priroda","italian")
r1.describe_restaurant()
r1.open_restaurant()
#9.2
print("---------9.2-----------")
restaraunt=Restaurant("Пузата хата","украинская")
restaraunt2=Restaurant("Казбек","грузинская")
restaraunt3=Restaurant("Амагама","Японская")
restaraunt.describe_restaurant()
restaraunt2.describe_restaurant()
restaraunt3.describe_restaurant()
print("---------9.4-----------")
p=int(input("Введите количество посетителей за день: "))
r1.set_number_served(p)
r1.increment_number_served()
#9.3
from User  import *

print("---------9.3-----------")
user1=User("Татару","Евгений",17)
user1.describe_user()
user1.greet_user()
#9.5
print("---------9.5-----------")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()

#9.6
class IceCreamStand(Restaurant):
    def __init__(self,resturant_name, cuisine_type):
        super().__init__(resturant_name, cuisine_type)
        self.flavors=["Пломбир","Сорбет","Щербет"]
    def type_icecream(self):
        print("Сорта мороженого:")
        for i in self.flavors:
            print(i)
#9.6
print("---------9.6-----------")        
IceCreamStand=IceCreamStand("Рожок","мороженое")
IceCreamStand.type_icecream()

#9.7
from Admin import *

#9.7
print("---------9.7-----------")  
admin1=Admin("Дмитриев","Денис",24)
admin1.greet_admin()

#9.8
from Admin import *
        
#9.8
print("---------9.8-----------")  
admin2=Privileges("Дмитриев","Денис",24)
admin2.show_privileges()
        
