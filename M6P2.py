quantity = int (input("Enter the quantity of an item: "))
unitPrice = 0.0

if quantity > 10000:
    unitPrice = 10.0
elif 5000 <= quantity <= 10000:
    unitPrice = 20.0
else:
    unitPrice = 30.0

extendedPrice = quantity * unitPrice
tax = extendedPrice * 0.07
total = extendedPrice + tax

print("Extended price: $", round(extendedPrice,2), sep="")
print("Tax: $", round(tax,2), sep="")
print("Total: $", round(total,2), sep="")