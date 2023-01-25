
## A function that takes in the ticker of a commodity and returns a number of relevant stats

def ticker_numbers(ticker):
    import yfinance as yf
    import json

    try:
        ticker_data = yf.Ticker(ticker)
        i_string = str(ticker_data.info)

        fifty_two_HIGH_length = 1359 - 1334
        fifty_two_LOW_length = 1474 - 1448
        two_hundred_AVG_length = 440 - 408
        regularMarketPrice_length = 1625 - 1596
        regularMarketPreviousClose_length = 660 - 624

        # fifty_two_HIGH = i["fiftyTwoWeekHigh"]
        # fifty_two_LOW = i["fiftyTwoWeekLow"]
        # two_hundred_AVG = i["twoHundredDayAverage"]
        two_hundred_AVG = float(i_string[i_string.find("twoHundredDayAverage"): (
                    i_string.find("twoHundredDayAverage") + two_hundred_AVG_length)].split(":")[1].strip().replace(",",
                                                                                                                   ""))
        fifty_two_HIGH = float(i_string[i_string.find("fiftyTwoWeekHigh"): (
                    i_string.find("fiftyTwoWeekHigh") + fifty_two_HIGH_length)].split(":")[1].strip().replace(",", ""))
        fifty_two_LOW = float(
            i_string[i_string.find("fiftyTwoWeekLow"): (i_string.find("fiftyTwoWeekLow") + fifty_two_LOW_length)].split(
                ":")[1].strip().replace(",", ""))

        prev_CLOSE = float(i_string[i_string.find("regularMarketPreviousClose"): (i_string.find("regularMarketPreviousClose") + regularMarketPreviousClose_length)].split(":")[1].strip().replace(",",""))
        reg_MARKET = float(i_string[i_string.find("regularMarketPrice"): (i_string.find("regularMarketPrice") + regularMarketPrice_length)].split(":")[1].strip().replace(",",""))

    except:
        ticker_data = yf.Ticker(ticker)
        fifty_two_HIGH = ticker_data.basic_info["year_high"]
        fifty_two_LOW = ticker_data.basic_info["year_low"]
        two_hundred_AVG = ticker_data.basic_info["two_hundred_day_average"]
        prev_CLOSE = ticker_data.basic_info["previous_close"]
        reg_MARKET = ticker_data.basic_info["last_price"]

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