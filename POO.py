# Object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to creat many objects

# cass = (blueprint) used to desing the structure and layout of an object


#class Car:
#    def __init__(self,model, year, color, for_sale):   #Usado para iniciar a construção de um objeto, (self) significa agora,
#        self.model = model                             # model,year,color são os atributos e for_sale é um metodo que pode ser true ou false
#        self.year = year
#        self.color = color
#        self.for_sale = for_sale
from ScriptPOO import Car

car1 = Car("Ferrari 812", 2020, "red", False)
car2 = Car("Corvette", 2016, "black", True)
car3 = Car("Charger", 2018, "black", False)

print(car1.model, car1.year, car1.color, car1.for_sale)
print(car2.model, car2.year, car2.color, car2.for_sale)
print(car3.model, car3.year, car3.color, car3.for_sale)

car2.drive()
car2.stop()
car1.describe()































