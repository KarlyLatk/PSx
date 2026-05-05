def compute_nextMonth(month, sales):
    percent = 0.0
    if month.lower() in ['mar', 'jan', 'feb']:
        percent = 0.10
    elif month.lower() in ['jun', 'apr', 'may']:
        percent = 0.15
    elif month.lower() in ['sep', 'jul', 'aug']:
        percent = 0.20
    elif month.lower() in ['dec', 'oct', 'nov']:
        percent = 0.25

    months_sale = sales * (1+percent)

    return months_sale

start = str(input("This program computes the forecast percent of sales for the month per representative. Enter (y/n) to start or stop the program. "))

while start.lower() == "y":
    last = str(input("Enter the last name of the sales representative: "))
    month = str(input("Enter the month of the sale (first three letters): "))
    sale = float(input("Enter the number of sales: "))

    print("Next month's sales: ", compute_nextMonth(month, sale))

    start = str(input("Do you want to enter another sale representative? (y/n): "))