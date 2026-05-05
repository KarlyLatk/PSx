def discount(quantity, price, discount_rate):
    total = quantity * price
    discount_amount = total * discount_rate
    discount_price = total - discount_amount

    return discount_amount, discount_price

quantity = int(input("Enter the quantity of the item: "))
price = float(input("Enter the price of the item: "))
rate = float(input("Enter the discount rate of the item: "))

discount_amount, discount_price = discount(quantity, price, rate)

print("Discount amount: $", discount_amount, sep="")
print("Discount price: $", discount_price, sep="")
print("Quantity: ", quantity)
print("Price: $", price, sep="")