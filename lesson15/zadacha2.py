name_1={"Deniasdsds":24,"Zheasdka":17,"Vovasda":15,"Boasdasdgdan":17,"Mishasddsada":2}
name={"Denis":24,"Zheka":17,"Vova":15,"Bogdan":17,"Misha":2}
our_cars={"Tiger Porshe":1943,"Camaro":1984,"Ferrari":103,"Lada":2004,"Bugati":2000}
#metod 1
python = name.copy()
python.update(our_cars)
print(python)
#metod2
olds=name | our_cars | name_1
print(olds)
