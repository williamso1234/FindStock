import yfinance as YahooFinance

GetApplovinInformation = YahooFinance.Ticker("APP")

history = GetApplovinInformation.history(period="1d")

LOTD = history["Low"].iloc[0]
HOTD = history["High"].iloc[0]

print("The low of the day is", LOTD)
print("The high of the day is", HOTD)
