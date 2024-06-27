import yfinance as YahooFinance

GetApplovinInformation = YahooFinance.Ticker("APP")

history = GetApplovinInformation.history(period="max")

PSU = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


def latest_unlocked_psu(history, PSU):
    unlocked_price = None
    unlocked_date = None
    for Price_point in PSU:
        DaysInRow = 0
        for date, price in history['Close'].items():
            if price >= Price_point:
                DaysInRow += 1
                if DaysInRow >= 30:
                    unlocked_price = Price_point
                    unlocked_date = date
                    break
            else:
                DaysInRow = 0
        if DaysInRow < 30:
            break
    return unlocked_price, unlocked_date


unlocked_price, unlocked_date = latest_unlocked_psu(history, PSU)
print("The latest unlocked price price is:", unlocked_price, " at", unlocked_date )
