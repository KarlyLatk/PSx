r = str(input("Do you want to start this program?: "))
count = 0
while r.lower() == "yes":
    last = str(input("Enter your last name: "))
    exam1 = float(input("Enter your first exam score: "))
    exam2 = float(input("Enter your second exam score: "))

    averageScore = (exam1+exam2)/2
    count += 1
    print(last, averageScore, sep=" ")

    r = str(input("Do you want to enter another student?: "))

print("Number of students who entered data: ", count)

