def finish_price(msrp, make, model, type):
    percent_off = 0.0
    if make.lower() == "honda" and model.lower() == "accord":
        percent_off = 0.10
    elif make.lower() == "toyota" and model.lower() == "rav4":
        percent_off = 0.15
    elif type.lower() == "y":
        percent_off = 0.30
    else:
        percent_off = 0.05

    new_msrp = (msrp - (msrp * percent_off)) + (0.07 * msrp)

    return new_msrp


sum_total = 0.0
sum_msrp = 0.0
start = str(input("This program computes the percent off MSRP for a car. Enter (y/n) to start or stop the program. "))

while start.lower() == "y":
    make = str(input("Enter the make of the car: "))
    model = str(input("Enter the model of the car: "))
    type = str(input("Is the vehicle electric? (y/n): "))
    msrp = float(input("Enter the MSRP (sticker price) of the car: "))

    total = finish_price(msrp, make, model, type)
    sum_total += total

    sum_msrp += msrp
    print("Final sale price of car: $", total, sep="")

    start = str(input("Do you want to enter another car? (y/n): "))

print("Sum of all MSRP's: $", sum_msrp, sep="")
print("Sum of all sales price: $", sum_total, sep="")