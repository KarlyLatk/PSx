purchasePricePerShare = float(input("Enter the purchase price per share: "))
currentStockPrice = float(input("Enter the current stock price: "))
quantityOfStock = int(input("Enter the quantity of stock: "))
value = (currentStockPrice-purchasePricePerShare)*quantityOfStock

print("The value of the stock entered is $", round(value, 2))