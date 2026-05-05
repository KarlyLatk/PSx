def exam_average(exam1, exam2, exam3):
    total_points = exam1 + exam2 + exam3
    average = total_points / 3


    return average, total_points

student = str(input("Enter student's name: "))
exam1 = float(input("Enter exam 1: "))
exam2 = float(input("Enter exam 2: "))
exam3 = float(input("Enter exam 3: "))

average, total_points = exam_average(exam1, exam2, exam3)

print(student)
print("Total points: ", total_points)
print("Exam average: ", round(average, 2))