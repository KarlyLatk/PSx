principle = int (input("Enter the principle amount of a CD: "))
years = int(input("Enter the year(s) to maturity of the CD: "))

interest = 0.0

if principle > 100000 and years == 5:
    interest = 0.06
elif 50000 <= principle <= 100000:
    if years == 10:
        interest = 0.05
    elif years == 5:
        interest = 0.04
    else:
        interest = 0.02
else:
    interest = 0.02

firstInterest = principle * interest
print("Principle amount: $", principle, sep="")
print("Interest rate: ", interest)
print("Interest amount for first year: $", round(firstInterest,2), sep="")