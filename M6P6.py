lastName = str(input("Input your last name: "))
salary = float(input("Input your salary: "))
level = int(input("Input your job level: "))

bonusRate = 0.0
if level >= 10:
    bonusRate = 0.25
elif 5 <= level <= 9:
    bonusRate = 0.20
else:
    bonusRate = 0.10

bonus = salary * bonusRate
print(lastName, " bonus: $", round(bonus,2), sep="")