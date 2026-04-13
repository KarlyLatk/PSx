with open('products.txt') as f:
    i=0
    extendedPriceSum = 0.0
    orderCount = 0
    averageOrderPrice = 0.0
    averageOrderQuantity = 0.0
    itemCount = 0

    lines = f.readlines()
    while i < len(lines):
        name = lines[i].rstrip()
        quantity = int(lines[i+1].rstrip())
        price = float(lines[i+2].rstrip())

        extendedPrice = quantity * price
        extendedPriceSum += extendedPrice
        orderCount += quantity
        itemCount +=1

        print(name, " ", quantity, " $", price, " $", extendedPrice, sep="")
        i+=3
averageOrderPrice = extendedPriceSum / orderCount
averageOrderQuantity = orderCount / itemCount

print("Sum of all the extended prices: $", extendedPriceSum, sep="")
print("Count of the number of orders: ", orderCount)
print("Average order price: $", round(averageOrderPrice,2), sep="")
print("Average order quantity: ", round(averageOrderQuantity, 2))
f.close()
