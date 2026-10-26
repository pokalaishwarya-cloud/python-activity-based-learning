balance = 0.0
transactions = []

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Transaction Summary")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        amount = float(input("Enter deposit: "))
        if amount > 0:
            balance += amount
            transactions.append(("Deposit", amount))
            print("Deposit successful")
        else:
            print("Invalid amount")

    elif choice == "2":
        amount = float(input("Enter withdrawal: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount <= balance:
            balance -= amount
            transactions.append(("Withdrawal", amount))
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    elif choice == "3":
        for transaction, amount in transactions:
            print(transaction, "Rs.", amount)
        print("Current balance: Rs.", round(balance, 2))

    elif choice == "4":
        print("Thank you")
        break

    else:
        print("Invalid option")
