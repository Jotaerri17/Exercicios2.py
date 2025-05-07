# Polimorphism = Greek word that means to "have many forms or faces"
#                Poly = many
#                Morphe = Form

# 1. Inheritance = An object could be treated of the same type as a parent class
# 2. "Duck typing" = Object must have necessary attributes/methods


# from abc import ABC, abstractmethod
#
# class Shape:
#
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#       self.radius = radius
#
#     def area(self):
#         return 3.14 * (self.radius ** 2)
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return (self.base * self.height) / 2
#
#
# class Pizza(Circle):
#     def __init__(self, cobertura, radius):
#         super().__init__(radius)
#         self.cobertura = cobertura
#
#
# shapes = [Circle(4), Square(5), Triangle(6,8), Pizza("portuguesa", 15)]
# for shape in shapes:
#     print(f"{shape.area()}cm^2")
#
#
#
# # "Duck typing" = Another way to achive polymorphism besides Inheritance
# #                 Object must have the minimum necessary attributes/methods
# #                 "If it looks like a duck and quacks like a duck, it must be a duck."
#
#
#
# class Animal:
#     alive = True
#
# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")
#
# class Cat(Animal):
#     def speak(self):
#         print("Meow!")
#
# class Car:
#
#     alive = False
#
#     def speak(self):
#         print("HONK!")
#
# animals = [Dog(), Cat()]
# for animal in animals:
#     animal.speak()
#     print(animal.alive)




# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for genereal utillity functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utllity functions that do not need acess to class data



# class Employee:
#
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#     def get_info(self):
#         return f"{self.name} = {self.position}"
#
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions = ["Manager","Cashier","Cook","Janitor"]
#         return position in valid_positions
#
#
# employee1 = Employee("Eugene", "Manager")
# employee2 = Employee("JR", "Cashier")
# employee3 = Employee("Spongebob", "Cook")
#
# print(Employee.is_valid_position("Cook"))
# print(employee1.get_info())
# print(employee2.get_info())
# print(employee3.get_info())




# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself


class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"


student1 = Student("João", 4.8)
student2 = Student("Pedro", 5.0)
student3 = Student("Nath", 3.2)

print(Student.get_count())
print(Student.get_average_gpa())



# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = best for class-level data or require access to the class itself













