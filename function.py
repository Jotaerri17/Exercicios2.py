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


