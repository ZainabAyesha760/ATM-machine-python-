"""
Simple ATM Machine Simulation in Python
Author: ZA
"""

def display_menu():
    print("\n" + "="*25)
    print("  ATM MACHINE")
    print("="*25)
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("="*25)

def check_balance(balance):
    print(f"\nYour current balance is: Rs. {balance}")

def deposit(balance):
    try:
        amount = int(input("Enter amount to deposit: Rs. "))
        if amount <= 0:
            print("Please enter a positive amount.")
            return balance
        balance += amount
        print(f"Successfully deposited Rs. {amount}")
        print(f"New balance is: Rs. {balance}")
    except ValueError:
        print("Invalid input! Please enter numbers only.")
    return balance

def withdraw(balance):
    try:
        amount = int(input("Enter amount to withdraw: Rs. "))
        if amount <= 0:
            print("Please enter a positive amount.")
            return balance
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"Withdrawal successful! You withdrew Rs. {amount}")
            print(f"Remaining balance is: Rs. {balance}")
    except ValueError:
        print("Invalid input! Please enter numbers only.")
    return balance

def main():
    balance = 1000
    print("Welcome to Python ATM!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("\nThank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice! Please select from 1 to 4.")

if __name__ == "__main__":
    main()
