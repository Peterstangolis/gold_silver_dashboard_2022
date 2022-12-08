
## function that retrieves data from yfinance for the time period and interval specified

def one_day_data(period, interval, ticker):
    import yfinance as yf

    ticker_data = yf.Ticker(ticker)

    one_day_ticker_prices = ticker_data.history(period=period, interval=interval)
    last_updated = one_day_ticker_prices.index[-1]
    last_price = one_day_ticker_prices.Close[-1]

    return last_updated, last_price, one_day_ticker_prices

