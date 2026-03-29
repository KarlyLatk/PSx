last_name = str(input("Enter your last name: "))
midterm = float(input("Enter your midterm grade: "))
final_exam = float(input("Enter your final exam: "))

total_exam = (midterm*.40)+(final_exam*.60)

print(last_name, "total exam points is", round(total_exam))
