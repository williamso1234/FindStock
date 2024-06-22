import yfinance as YahooFinance

GetApplovinInformation = YahooFinance.Ticker("APP")

history = GetApplovinInformation.history(period="1y")

LOTY = history["Low"].min()
DLOTY = history["Low"].idxmin()
HOTY = history["High"].max()
DHOTY = history["High"].idxmax()

print("The lowest price of the year was,", LOTY, "at the date of,", DLOTY)
print("The highest price of the year was,", HOTY, "at the date of,", DHOTY)