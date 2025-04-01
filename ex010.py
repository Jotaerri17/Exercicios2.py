# Class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

#class Student:

#    class_year = 2025
#    num_students = 0

#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#        Student.num_students += 1

#student1 = Student("Pedro", 30)
#student2 = Student("Paulo", 25)
#student3 = Student("Maria", 20)
#student4 = Student("Ana", 22)

#print(f"My graduating class of {student1.class_year} will have {Student.num_students} students.")
#print(student1.name)
#print(student2.name)
#print(student3.name)
#print(student4.name)


# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(parent)

#class Animal:
#    def __init__(self, name):
#        self.name = name
#        self.is_alive = True
#    def eat(self):
#        print(f"{self.name} is eating...")

#   def sleep(self):
#        print(f"{self.name} is asleep...")

#class Dog(Animal):
#    def speak(self):
#        print(f"{self.name} says woof!")

#class Cat(Animal):
#    def speak(self):
#        print(f"{self.name} says meow!")

#class Mouse(Animal):
#    def speak(self):
#        print(f"{self.name} says squeak!")

#dog = Dog("Scooby")
#cat = Cat("Garfield")
#mouse = Mouse("Mickey")













