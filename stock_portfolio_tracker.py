
# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock_name = input("Enter stock symbol: ").upper()
    quantity = int(input("Enter quantity: "))
    portfolio[stock_name] = quantity

print("\nPortfolio Summary")
print("-" * 30)

for stock, quantity in portfolio.items():
    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment
        print(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${investment}")
    else:
        print(f"{stock}: Stock price not available")

print("-" * 30)
print("Total Investment Value = $", total_investment)

with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-------------------------\n")

    for stock, quantity in portfolio.items():
        if stock in stock_prices:
            investment = stock_prices[stock] * quantity
            file.write(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${investment}\n")

    file.write(f"\nTotal Investment Value = ${total_investment}")

print("\nPortfolio summary saved in portfolio_summary.txt")
