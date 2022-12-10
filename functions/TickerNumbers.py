
## A function that takes in the ticker of a commodity and returns a number of relevant stats

def ticker_numbers(ticker):
    import yfinance as yf
    import json

    ticker_data = yf.Ticker(ticker)


    fifty_two_HIGH = ticker_data.info["fiftyTwoWeekHigh"]
    fifty_two_LOW = ticker_data.info["fiftyTwoWeekLow"]
    two_hundred_AVG = ticker_data.info["twoHundredDayAverage"]
    prev_CLOSE = ticker_data.info["previousClose"]
    reg_MARKET = ticker_data.info["regularMarketPrice"]
    price_change = reg_MARKET - prev_CLOSE
    perc_change = round((price_change / prev_CLOSE) * 100, 3)

    updated_numbers = {
        'fifty_two_HIGH' : fifty_two_HIGH,
        "fifty_two_LOW" : fifty_two_LOW,
        "two_hundred_AVG" : two_hundred_AVG,
        "prev_CLOSE" : prev_CLOSE,
        "reg_MARKET" : reg_MARKET,
        "price_change": price_change,
        "perc_change" : perc_change
    }

    with open("data/updated_numbers.json", "w") as outfile:
        json.dump(updated_numbers, outfile)

    #json_object = json.dumps(updated_numbers, indent=4)


    #return fifty_two_HIGH, fifty_two_LOW, two_hundred_AVG, prev_CLOSE, reg_MARKET, price_change, perc_change