days = int(input("Enter number of days: "))

if days <= 0:
    print("Invalid number of days")
else:
    for i in range(1, days + 1):
        prepared = float(input("Enter meals prepared: "))
        served = float(input("Enter meals served: "))

        if prepared <= 0 or served < 0 or served > prepared:
            print("Invalid meal quantities")
            continue

        leftover = prepared - served
        waste_percent = leftover / prepared * 100

        print("Day", i)
        print("Leftover meals:", leftover)
        print("Waste percentage:", round(waste_percent, 2), "%")

        if waste_percent > 10:
            print("Warning: Excessive food waste")
        else:
            print("Food waste is within the limit")
