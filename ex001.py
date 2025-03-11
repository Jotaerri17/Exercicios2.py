#shopping cart progam

foods=[]
prices=[]
total=0
while True:
    food=input("Enter the food to by (q to quit):")
    if food.lower() == "q":
        break
    else:
        price=float(input(f"Enter the price of a {food} $"))
        foods.append(food)
        prices.append(price)

print("------ YOUR CART ------")
for food in foods:
    print(food , end=" ")

for price in prices:
    total+=price
print(f"\n Your total is: ${total}")





















