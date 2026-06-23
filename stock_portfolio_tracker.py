import csv
import os

# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOGL": 140,  # Google
    "AMZN": 178,   # Amazon
    "MSFT": 415,   # Microsoft
    "META": 505,   # Meta
    "NFLX": 628,   # Netflix
}

def display_available_stocks():
    print("\n📈 Available Stocks:")
    print("-" * 30)
    print(f"{'Symbol':<10} {'Price (USD)':>10}")
    print("-" * 30)
    for symbol, price in stock_prices.items():
        print(f"{symbol:<10} ${price:>9}")
    print("-" * 30)

def get_portfolio():
    portfolio = {}
    print("\nEnter stock symbol and quantity (type 'done' when finished):")

    while True:
        symbol = input("\nStock symbol: ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in stock_prices:
            print(f"❌ '{symbol}' not found. Please choose from the available stocks above.")
            continue

        try:
            quantity = int(input(f"Quantity of {symbol} shares: ").strip())
            if quantity <= 0:
                print("❌ Quantity must be a positive number.")
                continue
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if symbol in portfolio:
            portfolio[symbol] += quantity
            print(f"✅ Updated {symbol}: total {portfolio[symbol]} shares.")
        else:
            portfolio[symbol] = quantity
            print(f"✅ Added {symbol} x{quantity}")

    return portfolio

def display_portfolio(portfolio):
    if not portfolio:
        print("\n⚠️  No stocks in portfolio.")
        return 0

    total_investment = 0
    print("\n" + "=" * 45)
    print("         📊 YOUR STOCK PORTFOLIO")
    print("=" * 45)
    print(f"{'Symbol':<10} {'Qty':>5} {'Price':>10} {'Value':>12}")
    print("-" * 45)

    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]
        value = price * quantity
        total_investment += value
        print(f"{symbol:<10} {quantity:>5} ${price:>9} ${value:>11,.2f}")

    print("-" * 45)
    print(f"{'TOTAL INVESTMENT':>32}  ${total_investment:>11,.2f}")
    print("=" * 45)

    return total_investment

def save_to_txt(portfolio, total_investment):
    filename = "portfolio_report.txt"
    with open(filename, "w") as f:
        f.write("STOCK PORTFOLIO REPORT\n")
        f.write("=" * 45 + "\n")
        f.write(f"{'Symbol':<10} {'Qty':>5} {'Price':>10} {'Value':>12}\n")
        f.write("-" * 45 + "\n")
        for symbol, quantity in portfolio.items():
            price = stock_prices[symbol]
            value = price * quantity
            f.write(f"{symbol:<10} {quantity:>5} ${price:>9} ${value:>11,.2f}\n")
        f.write("-" * 45 + "\n")
        f.write(f"{'TOTAL INVESTMENT':>32}  ${total_investment:>11,.2f}\n")
    print(f"\n✅ Report saved as '{filename}'")

def save_to_csv(portfolio, total_investment):
    filename = "portfolio_report.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price (USD)", "Value (USD)"])
        for symbol, quantity in portfolio.items():
            price = stock_prices[symbol]
            value = price * quantity
            writer.writerow([symbol, quantity, price, f"{value:.2f}"])
        writer.writerow([])
        writer.writerow(["", "", "Total Investment", f"{total_investment:.2f}"])
    print(f"\n✅ Report saved as '{filename}'")

def main():
    print("=" * 45)
    print("    💼 STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    display_available_stocks()

    portfolio = get_portfolio()

    total_investment = display_portfolio(portfolio)

    if portfolio:
        save_choice = input("\nSave report? (txt / csv / no): ").lower().strip()
        if save_choice == "txt":
            save_to_txt(portfolio, total_investment)
        elif save_choice == "csv":
            save_to_csv(portfolio, total_investment)
        else:
            print("📁 Report not saved.")

    again = input("\nTrack another portfolio? (yes / no): ").lower().strip()
    if again == "yes":
        main()
    else:
        print("\nThank you for using Stock Portfolio Tracker! Goodbye 👋")

if __name__ == "__main__":
    main()
