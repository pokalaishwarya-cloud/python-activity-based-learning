held = int(input("Enter total classes held: "))
attended = int(input("Enter classes attended: "))

if held <= 0 or attended < 0 or attended > held:
    print("Invalid attendance details")
else:
    percentage = attended / held * 100

    print("Attendance percentage:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Eligible for examination")
    else:
        print("Not eligible for examination")

        required = (75 * held - 100 * attended) / 25
        if required > 0:
            print("Minimum additional classes to attend:",
                  int(required))
