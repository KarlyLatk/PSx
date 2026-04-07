partNum = int (input("Enter a part number: "))
quantity = int (input("Enter a quantity: "))

unitCost = 0.0

if partNum == 10 or partNum == 55:
    unitCost = 1.00
elif partNum == 99:
    unitCost = 2.00
elif partNum == 80 or partNum == 70:
    unitCost = 3.00
else:
    unitCost = 5.00

total = quantity * unitCost
print("Part number: ", partNum)
print("Cost per unit: $", unitCost, sep="")
print("Total cost: $", total, sep="")