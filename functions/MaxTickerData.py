
## A function that retrieves the max time period available for a particular ticker

def max_ticker_data(period, interval, ticker):
    import yfinance as yf

    ticker_data = yf.Ticker(ticker)

    max_data_ticker_prices = ticker_data.history(period=period, interval=interval)
    last_updated = max_data_ticker_prices.index[-1]
    last_price = max_data_ticker_prices.Close[-1]

    return last_updated, last_price, max_data_ticker_prices

