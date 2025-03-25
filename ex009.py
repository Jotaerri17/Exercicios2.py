#Python banking Program

#def show_balance(balance):
#    print(f"Your balance is: ${balance: .2f}")

#def deposit():
#    amount=float(input("Enter the amount to deposit:")).strip()
#    if amount < 0:
#        print("Invalid amount. Please try again.")
#        return 0
#    else:
#        return amount
#
#def withdraw(balance):
#    amount=float(input("Enter the amount to withdraw:")).strip()

#    if amount>balance:
#        print("Insufficient funds. Please try again.")
#        return 0
#    elif amount < 0:
#        print("Amount must be greater than 0. Please try again.")
#        return 0
#    else:
#        return amount
#def main():
#    balance = 0
#    is_running = True

#    while is_running:
#        print("Welcome to Python Banking Program")
#        print("-=" *25)
#        print("1 - show balance")
#        print("2 - deposit")
#        print("3 - withdraw")
#        print("4 - exit")
#        print("-=" * 25)
#        choice = input("Enter your choice: ").strip()
#        if choice == "1":
#            show_balance(balance)
#        elif choice == "2":
#            balance+=deposit()
#        elif choice == "3":
#            balance-=withdraw(balance)
#        elif choice == "4":
#            is_running = False #Serve como o break
#        else:
#            print("Invalid choice. Please try again.")
#    print("-=" * 25)
#    print("Thank you! Have a nice day.")
#    print("-=" * 25)
#if __name__ == '__main__':
#    main()


# Python slot machine

import random
def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "💫"]
    results=[]
    return [ random.choice(symbols) for _ in range(3)]
def print_row(row):
    print("-=" * 7)
    print(" | ".join(row))
    print("-=" * 7)
def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 4
        elif row[0]== "🍉":
            return bet * 5
        elif row[0]=="🍋":
            return bet * 8
        elif row[0]=="🔔":
            return bet * 3
        elif row[0]=="💫":
            return bet * 20
    return 0
def main():
    balance= 100
    print("-=" *25)
    print("Welcome to Python Slot Machine")
    print("Symbols: 🍒 🍉 🍋 🔔 💫")
    print("-=" * 25)

    while balance > 0:
        print(f"Current balance is: ${balance: .2f}")
        bet = input("Place your bet amount:").strip()
        if  not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet= int(bet)

        if bet > balance:
            print("Insufficient funds. Please try again.")
            continue

        if bet <=0:
            print("Bet must be greater than 0. Please try again.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout=get_payout(row,bet)

        if payout > 0:
            print(f"You won ${payout: .2f}")
        else:
            print("Sorry, no winners this time.")
        balance += payout

        play_again= input("DO you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

    print("-=" * 25)
    print(f"Game over! Your final balance is: ${balance: .2f}")
    print("-=" * 25)

if __name__ == '__main__':
    main()




