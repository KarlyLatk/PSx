quantity = int (input("Enter the quantity of an item: "))
unitPrice = 0.0

if quantity >= 1000:
    unitPrice = 3.0
else:
    unitPrice = 5.0

extendedPrice = quantity * unitPrice
tax = extendedPrice * 0.07
total = extendedPrice + tax

print("Quantity:", quantity)
print("Unit price: $", round(unitPrice,2), sep="")
print("Extended price: $", round(extendedPrice,2), sep="")
print("Tax: $", round(tax,2), sep="")
print("Total: $", round(total,2), sep="")