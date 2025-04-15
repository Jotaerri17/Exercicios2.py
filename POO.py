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
#from ScriptPOO import Car

#car1 = Car("Ferrari 812", 2020, "red", False)
#car2 = Car("Corvette", 2016, "black", True)
#car3 = Car("Charger", 2018, "black", False)

#print(car1.model, car1.year, car1.color, car1.for_sale)
#print(car2.model, car2.year, car2.color, car2.for_sale)
#print(car3.model, car3.year, car3.color, car3.for_sale)

#car2.drive()
#car2.stop()
#car1.describe()


#class Block:
#    def __init__(self, dimensions):
        # Atributos de largura, comprimento e altura a partir da lista
#        self.width = dimensions[0]
#        self.length = dimensions[1]
#        self.height = dimensions[2]

#    def get_width(self):
#        return self.width

#    def get_length(self):
#        return self.length

#    def get_height(self):
#        return self.height

#    def get_volume(self):
#        return self.width * self.length * self.height

#    def get_surface_area(self):
#        return 2 * (self.width * self.length + self.width * self.height + self.length * self.height)


#b = Block([2, 4, 6])
#print(b.get_width())
#print(b.get_length())
#print(b.get_height())
#print(b.get_volume())
#print(b.get_surface_area())


# multiple inheritance = inherit from more than one parent class
#                         C(A,B)

# multilevel inheritence = inherit from a parent which inherits from another parents
#                          C(B) <- B(A) <- A

#class Animal:
#    def __init__(self, name):
#        self.name = name

#    def eat(self):
#        print(f"{self.name} is eating")

#    def sleep(self):
#        print(f"{self.name}is sleeping")

#class Prey(Animal):
#    def flee(self):
#        print(f"{self.name} is fleeing.")

#class Predator(Animal):
#    def hunt(self):
#        print(f"{self.name} is hunting.")

#class Rabbit(Prey):
#    pass

#class Hawk(Predator):
#    pass

#class Fish(Prey,Predator):
#    pass

#rabbit = Rabbit("Bugs")
#hawk = Hawk("Tony")
#fish = Fish("Nemo")


# super() = Fuction used in a child class to call methods from a parent class(superclass)
#           Allows you to extend the functionality of the inherited methods


class Comum:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and  {"filled" if self.filled else "unfilled"}.")

class Circle(Comum):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14 * (self.radius ** 2)}cm^2.")



class Square(Comum):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width * self.width}cm^2.")

class Triangle(Comum):
    def __init__(self, color, filled, width, heigth):
        super().__init__(color, filled)
        self.width = width
        self.heigth = heigth

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {(self.heigth * self.width) / 2}cm^2.")

circle = Circle('red', True, 5)
square = Square(color='blue', filled=False, width=5)
Triangle = Triangle('orange', False, 5, 5)
print(f"{circle.color}, {circle.filled}, {circle.radius}cm")
print(f"{square.color}, {square.filled}, {square.width}cm")
print(f"{Triangle.color}, {Triangle.filled}, {Triangle.width}cm")
Triangle.describe()
circle.describe()
square.describe()


























