name = input("Enter student name: ")

marks = []
for i in range(3):
    mark = int(input("Enter marks: "))
    if mark < 0 or mark > 100:
        print("Invalid marks")
        break
    marks.append(mark)

if len(marks) == 3:
    total = sum(marks)
    average = total / 3

    print("Student name:", name)
    print("Total marks:", total)
    print("Average:", round(average, 2))

    if min(marks) < 35:
        print("Result: Fail")
    elif average >= 75:
        print("Result: Distinction")
    elif average >= 60:
        print("Result: First Class")
    else:
        print("Result: Pass")
