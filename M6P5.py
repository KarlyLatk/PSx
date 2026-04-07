numTickets = int(input("Input the number of concert tickets: "))
pricePerTicket = 0

if numTickets >= 25:
    pricePerTicket = 50
elif 10 <= numTickets <= 24:
    pricePerTicket = 60
elif 5 <= numTickets <= 9:
    pricePerTicket = 70
else:
    pricePerTicket = 75

total = numTickets * pricePerTicket
print("Number of tickets: ", numTickets)
print("Price per ticket: $", pricePerTicket, sep="")
print("Total cost: $", round(total,2), sep="")