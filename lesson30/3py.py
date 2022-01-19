class Car:
    def __init__(self,marka,model,age):
        self.marka=marka
        self.model=model
        self.age=age
        self.adomiter=0
    def get_discript_name(self):
        print(f"Машина марки {self.marka}, модель-{self.model} {self.age} года!")
    def read_adomiter(self):
        print(f"Пробег машины равен {self.adomiter}")
    def update_adomiter(self,n):
        if n>=self.adomiter:
             self.adomiter=n
        else:print("Пробег изменить нельзя!!!")
    def increment_adomiter(self,m):
        self.adomiter+=m
        print(f"Теперь пробег составляет {self.adomiter}")

class Electrp_car(Car):
    def __init__(self,marka,model,age):
        Car.__init__(self,marka,model,age)
        self.butareya=0
    def name_electro_car(self):
        print(f"Електро-машина марки {self.marka}, модель-{self.model} {self.age} года!")   
    def new_butareya(self,but):
        self.butareya=but
        print(f"Батарея модели-{self.butareya}")
mine_new_car=Car("BMW","X6",1997)
mine_new_car.get_discript_name()
mine_new_car.adomiter=23
n=int(input("Введите значения пробега- "))
mine_new_car.update_adomiter(n)
mine_new_car.read_adomiter()
m=int(input("Введите значения вашего пробега после проката- "))
mine_new_car.increment_adomiter(m)
mine_new_electro_car=Electrp_car("Tesla","X",2010)
but=input("ведите модель батареии- ")
mine_new_electro_car.name_electro_car()
mine_new_electro_car.new_butareya(but)
