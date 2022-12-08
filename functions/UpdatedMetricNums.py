

## A function that takes in a ticker along with the one day values for the ticker and returns a metric that incorporates
##  the latest price, the change in price from previousclose along with a line chart in the background

#from functions.OneDayData import one_day_data
from variables import one_day_period, fiveMinute_interval, candle_fall, candle_rise
from functions.TickerNumbers import ticker_numbers

import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def updated_metric(ticker, title_name, line_color):
    from functions.OneDayData import one_day_data


    lu, lp, data = one_day_data(period=one_day_period, interval=fiveMinute_interval, ticker=ticker)


    fifty_two_week_HIGH, fifty_two_week_LOW, two_hundred_day_AVG, previous_CLOSE, \
    reg_MARKET, price_change, percent_change, updated_date = ticker_numbers(ticker=ticker)

    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=round(reg_MARKET, 3),
        number={"prefix": "$"},
        number_font=dict(size=70, color='#182033'),
        delta={"reference": previous_CLOSE, "valueformat": ".3f", 'relative': False,
               "suffix": f" ({percent_change:.2f}%)"},
        # domain = {'x':[1, 1], 'y':[0.5,0]},
        delta_decreasing=dict(color=candle_fall),
        delta_increasing=dict(color=candle_rise),
        delta_font=dict(size=24),
        title={
            "text": f"<span style='font-size:30px;color:#182033;'>{title_name} ({ticker})</span><br><span style='font-size:18px;color:#4C5958;'>{updated_date:%a %b %#d, %Y %H:%M%p}</span>"}
    ))

    fig.add_trace(go.Scatter(
        x=data.index,
        y=data["Close"],
        line_color=line_color,
        opacity=0.6))

    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    fig.update_layout(template='plotly_white',
                      width=500,
                      height=400)

    # fig.show()
    fig.write_html(f"data/{title_name}_metric_price.html")