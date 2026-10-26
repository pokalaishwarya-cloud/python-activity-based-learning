students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

if students <= 0 or subjects <= 0:
    print("Invalid number of students or subjects")
else:
    marks = []

    for i in range(students):
        row = []
        print("Enter marks for student", i + 1)

        for j in range(subjects):
            mark = int(input("Enter mark: "))
            row.append(mark)

        marks.append(row)

    for i in range(students):
        total = sum(marks[i])
        average = total / subjects

        print("Student", i + 1, "marks:", marks[i])
        print("Total:", total)
        print("Average:", round(average, 2))

    for j in range(subjects):
        subject_total = 0

        for i in range(students):
            subject_total += marks[i][j]

        print("Subject", j + 1,
              "average:", round(subject_total / students, 2))
