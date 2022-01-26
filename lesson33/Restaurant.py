#9.1
class Restaurant:
    def __init__(self,resturant_name, cuisine_type):
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type
        #9.4{
        self.number_served=0
        #9.4}
    def describe_restaurant(self):
        print(self.resturant_name,self.cuisine_type)
    def open_restaurant(self):
        print(f"Ресторан {self.resturant_name} с {self.cuisine_type} кухней открыт!")
         #9.4{
    def set_number_served(self,p):
        self.number_served=p
        print(f"Количество посетителей: {self.number_served}")
    def increment_number_served(self):
        self.number_served+=10
        print(f"Количество посетителей: {self.number_served}")
         #9.4}
