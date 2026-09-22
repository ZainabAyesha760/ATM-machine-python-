balance = 1000

while True:
    print("\n--- ATM Machine ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice: ").lower()

    if choice == "1" or choice == "check balance":
        print(f"Your current balance is: {balance}")

    elif choice == "2" or choice == "deposit":
        amount = int(input("How much money you wanted to deposit? "))
        balance = balance + amount
        print(f"Your current balance after deposit is: {balance}")

    elif choice == "3" or choice == "withdraw":
        amount = int(input("How much you wanted to withdraw? "))
        if amount <= balance and amount > 0:
            balance = balance - amount
            print(f"Withdrawal successful! Your remaining balance is: {balance}")
        else:
            print("Insufficient balance!")

    elif choice == "4" or choice == "exit":
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice, try again!")
