balance = float(input("Enter opening balance: "))

if balance < 0:
    print("Invalid opening balance")
else:
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("Deposit successful")
            else:
                print("Invalid amount")

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Invalid amount")
            elif amount <= balance:
                balance -= amount
                print("Withdrawal successful")
            else:
                print("Insufficient balance")

        elif choice == "3":
            print("Current balance: Rs.", round(balance, 2))

        elif choice == "4":
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")
