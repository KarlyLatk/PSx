ticker = str(input("Enter the stock ticker symbol for the company: "))
num_shares = int(input("Enter the number of shares the company has: "))
cost_shares = float(input("Enter the cost per share: "))

amount_invested = num_shares*cost_shares

print(ticker, "has $", round(amount_invested, 2), "amount invested")

