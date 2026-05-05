def compute_total(qty, unitprice):
    total = qty * unitprice
    if total >= 100000:
        discount = total * 0.10
        total = total - discount

    return total

start = str(input("This program tests for extended price of a product. Enter (y/n) to start or stop the program. "))
total_extended = 0.0
while start.lower() == "y":
    qty = int(input("Enter the quantity of the product: "))
    unitprice = float(input("Enter the price of the product: "))

    total = compute_total(qty, unitprice)
    print("Quantity: ", qty)
    print("Unit price: $", unitprice)
    print("Extended price: $", total)

    total_extended += total

    start = str(input("Do you want to enter another product? (y/n) "))

print("Total extended price for all items: $", total_extended)



