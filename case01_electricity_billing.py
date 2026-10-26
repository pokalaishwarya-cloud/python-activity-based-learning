units = int(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    total = bill + 50

    print("Energy charge: Rs.", bill)
    print("Fixed charge: Rs. 50")
    print("Total electricity bill: Rs.", total)
