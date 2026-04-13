with open('students.txt') as f:
    i = 0
    cost = 0.0
    tuitionSum = 0.0
    students = 0
    lines = f.readlines()
    while i < len(lines):
       name = lines[i].rstrip()
       district = lines[i+1].rstrip()
       credit = int(lines[i+2].rstrip())

       if district == "I":
           cost = 250.00
       else:
            cost = 500.00

       tuition = credit * cost
       tuitionSum += tuition
       students +=1
       print(name, " ", credit, " $", tuition, sep="")
       i+=3
print("Sum of all tuition owed: $",tuitionSum, sep="")
print("Number of students: ", students)

f.close()