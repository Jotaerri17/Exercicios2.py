# Function = A block of reusable code
#           place () after the function name to invoke it

#def happy(name, age):
#    print(f"Happy Birthday {name}!")
#    print(f"You are {age} years old!")
#    print(f"Happy Birthday to you {name}!")

#happy("joão", 19)

#def display(username, amount, date):
#    print(f"Hello {username}!")
#    print(f"You have ${amount:.2f} dollars in your account.")
#    print(f"Your account was created on {date}.")
#display("joão", 678.60, "17/05" )

# Return = Statement used to end a function
#          and send a result back to the caller

#def name(first, last):
 #   first = first.capitalize()
 #   last = last.capitalize()
 #   return first + " " + last
#full_name= name("João","rafael")
#print(full_name)

# Default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces #of arguments
#                     1. positional, 2. Default, 3. Keyword, 4. Arbitrary

#def net_price(price, discount=0,tax=0.05):
#    return price * (1 - discount) * (1 + tax)
#print(net_price(500))
#print(net_price(500,0.1))
#print(net_price(500,0.1,0))

#import time

#def count(end, start=0):
#    for x in range(start, end+1):
#        print(x)
#        time.sleep(0.5)
#    print("Done!")
#count(30,15)


# Keyword arguments = an argument peceded by an indetifier
#                     helps with readability
#                    orde of arguments doesn't matter
#                    1. positional, 2. Default, 3. Keyword, 4. Arbitrary


#def hello(greeting,title,first,last):
#    print(f"{greeting} {title} {first} {last}")

#hello("Hello",title="Mr.",first="joão",last="rafael") #Posição não importa quando declarado

#print("1","2","3","4","5", sep="-") #sep="-" separa os numeros com -

#def get_phone(country_code, area_code, first, last):
#    return f"{country_code}-{area_code}-{first}-{last}"
#phone_num=get_phone(country_code=55,area_code=79,first=9962,last=1709)
#print(phone_num)


# *args    = allows you to pass multiple non-key arguments
# **kwargs = allowa you to pass multiple keywords-arguments
#            * unpacking operator
#            1. positional, 2. Default, 3. Keyword, 4. Arbitrary

#def add(*args): #torna uma lista, pode ser usado qualquer nome contanto que tenha o (*)
#    total=0
#    for arg in args:
#        total+=arg
#    return total
#print(add(1,2,3))


#def print_address(**kwargs): #torna um dicionario
#    for key,value in kwargs.items():
#        print(f"{key}: {value}")
#print_address(street="123 Fake St.",
#              apt="104 nature",
#              city="Springfield",
#              state="IL",
#              zip="62701")

#def shipping_label(*args, **kwargs):
#    for arg in args:
#        print(arg,end=" ")
#    print()
#    if "apt" in kwargs:
#         print(f"{kwargs.get('street')} {kwargs.get('apt')}")
#    elif "pobox" in kwargs:
#         print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
#    else:
#         print(f"{kwargs.get('street')}")
#    print(f" {kwargs.get('state')},{kwargs.get('city')},{kwargs.get('zip')}")

#shipping_label("Dr.", "John", "Smith",
#               street="123 Fake St.",
#               pobox="104 nature",
#               city="Springfield",
#               state="IL",
#               zip="62701")

# Iterables = An object/collection that can return its elements
#              one at a time, allowing it to be iterated over in a loop


#n=int(input("Digite um numero:"))
#def num_fac(n):
 #   if n==0:
 #       return 1
 #   else:
 #       resultado= n*num_fac(n-1)
 #       return resultado
#print(f"O fatorial de {n} é",num_fac(n))

#Membership operators = used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in   2. not in

#word="APPLE"
#etter=input("Guess a letter in the secret word")

#if letter not in word:
#    print(f"There is no {letter} in the secret word ")
#else:
#    print(f"There is a {letter} in the secret word ")

#grades={"joao": "A",
#        "maria": "B",
#        "pedro": "A",
#        "ana": "C"}
#student=input("Enter the name of student:")
#if student  in grades:
#    print(f"{student} grade is {grades[student]}")
#else:
#    print(f"{student} is not in the database")

#email="jotaerri@gmail.com"
#if "@gmail" in email and ".com" in email:
#    print("This is a gmail")
#else:
#    print("This is not a gmail")


#List  comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

#doubles=[x*2 for x in range(1,11)]
#triples=[y*3 for y in range(11,21)]
#squares=[z*z for z in range(1,11)]

#fruits= ["apple","banana","cherry","orange"]
#fruit_chars=[fruit[0] for fruit in fruits]

#numbers=[1,-2,-3,4,-5,6]
#positive_nums=[num for num in numbers if num>=0]
#negative_numbers=[num for num in numbers if num<0]
#even_nums=[num for num in numbers if num % 2 == 0]
#odd_nums=[num for num in numbers if num % 2 == 1]


#grades=[85, 42,77,90, 69, 30, 17]
#passing_grades = [grade for grade in grades if grade >=60]

#Match-case statement (switch): An alternative to using many "elif" statements
#                               Execute some code if a value matches a "case"
#                               Benefits: cleaner and syntaxx is more readable

#def day_of_week(day):
#    match day:
#        case 1:
#            return " It is Monday"
#        case 2:
#            return " It is Tuesday"
#        case 3:
#            return " It is Wednesday"
#        case 4:
#            return " It is Thursday"
#        case 5:
#            return " It is Friday"
#        case _:  #botar case _ para substituir um else
#            return " It is Invalid day"

#print(day_of_week(5))

#def day_of_week(day):
#    match day:
#        case "Sunday" | "Saturday": # or == |
#            return True
#        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#            return False
#        case _:  #botar case _ para substituir um else
#            return " It is Invalid day"

#print(day_of_week("Monday"))


#Module = a file containing code you want to include in your program use "import" to
#         incluse a modulo (built-in or your own) useful to break up a large program
#         reusalble separte files

import exmodulo
from exmodulo import circumference

#pi= exmodulo.pi
#result= exmodulo.square(3)
#cube= exmodulo.cube(9)
#circumference=exmodulo.circumference(10)
#area=exmodulo.area(10)
#print(-cube,-circumference,-area,-result)


#Variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
# Ordem de onde é puxada a variavel

#from math import e

#def func1():
#    print(e)
#e=3
#func1()


#def happy_birthday(name, age):
#    print(f"Happy Birthday {name}!")
#    print(f"You are {age} years old!")
#def main():
#    name="jotaerri"
#    age= 19
#    happy_birthday(name, age)
#main()

#if __name__ == __main__: (this script can be imported OR run standalone)
#                         Functions and classes in this module can be reused
#                         without the main block of code executing

# ex.library = Import library for functionality
#              When running library directly, display a help page

#def main():
    #Your program goes here
#if __name__ == "__main__":
#    main()














