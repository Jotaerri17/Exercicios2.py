#Python banking Program

def show_balance(balance):
    print(f"Your balance is: ${balance: .2f}")

def deposit():
    amount=float(input("Enter the amount to deposit:"))
    if amount < 0:
        print("Invalid amount. Please try again.")
        return 0
    else:
        return amount

def withdraw(balance):
    amount=float(input("Enter the amount to withdraw:"))

    if amount>balance:
        print("Insufficient funds. Please try again.")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0. Please try again.")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True

    while is_running:
        print("Welcome to Python Banking Program")
        print("-=" *25)
        print("1 - show balance")
        print("2 - deposit")
        print("3 - withdraw")
        print("4 - exit")
        print("-=" * 25)
        choice = input("Enter your choice: ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance+=deposit()
        elif choice == "3":
            balance-=withdraw(balance)
        elif choice == "4":
            is_running = False #Serve como o break
        else:
            print("Invalid choice. Please try again.")
    print("-=" * 25)
    print("Thank you! Have a nice day.")
    print("-=" * 25)
if __name__ == '__main__':
    main()







