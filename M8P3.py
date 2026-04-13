with open('employees.txt') as f:
    i = 1
    bonusSum = 0.0
    lines = f.readlines()
    for line in lines:
        if i % 2 == 0:
            #even - salary
            salary = float(line)
            bonusRate = 0.0
            if salary >= 100000.00:
                bonusRate = 0.20
            elif salary == 50000.00:
                bonusRate = 0.15
            else:
                bonusRate = 0.10
            bonus = salary * bonusRate
            bonusSum += bonus
            print(line.rstrip(), " $", bonus, sep="")


        else:
            #odd - names
            print(line.rstrip(), " $", end="")
        i+=1
print("The bonus sum is: $", bonusSum, sep="")
f.close()