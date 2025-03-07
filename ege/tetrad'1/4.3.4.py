import yfinance as yf
import matplotlib.pyplot as plt


tickers = ["AAPL", "MSFT", "GOOG"]  
start_date = "2021-01-01"
end_date = "2021-12-31"


data = yf.download(tickers, start=start_date, end=end_date)


close_prices = data["Close"]


plt.figure(figsize=(12, 6))

for ticker in tickers:
    plt.plot(close_prices.index, close_prices[ticker], label=ticker)

plt.title("Динамика цен акций Apple, Microsoft и Google за 2021 год")
plt.xlabel("Дата")
plt.ylabel("Цена закрытия (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

