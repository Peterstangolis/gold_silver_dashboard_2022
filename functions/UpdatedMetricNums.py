import datetime

## A function that takes in a ticker along with the one day values for the ticker and returns a metric that incorporates
##  the latest price, the change in price from previousclose along with a line chart in the background

from functions.OneDayData import one_day_data
from variables import one_day_period, fiveMinute_interval, candle_fall, candle_rise, two_day_period
from functions.TickerNumbers import ticker_numbers

# Path Settings
from pathlib import Path

THIS_DIR = Path(__file__).parent if"__file___" in locals() else Path.cwd()

DATA_DIR = THIS_DIR / "data/updated_numbers.json"

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st



def updated_metric(ticker, title_name, line_color, fill_color):
    #from functions.OneDayData import one_day_data
    import json
    with open(DATA_DIR) as file:
        contents = file.read()
    parsed_contents = json.loads(contents)

    #p = two_day_period if datetime.datetime.today().weekday() == 6 else one_day_period
    lu, lp, data = one_day_data(period=two_day_period if datetime.datetime.today().weekday() == 6 else one_day_period,
                                interval=fiveMinute_interval, ticker=ticker)

    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode="number+delta",
        value= float(parsed_contents["reg_MARKET"]),
        number={"prefix": "$"},
        number_font=dict(size=70, color='#182033'),
        delta={"reference": parsed_contents["prev_CLOSE"], "valueformat": ".3f", 'relative': False,
               "suffix": f" ({parsed_contents['perc_change']:.2f}%)"},
        domain = {'x':[1, 1], 'y':[0.5,0]},
        delta_decreasing=dict(color=candle_fall),
        delta_increasing=dict(color=candle_rise),
        delta_font=dict(size=24),
    ))

    fig.add_trace(go.Scatter(
        x=data.index,
        y=data["Close"],
        line_color=line_color,
        line_width=0.8,
        opacity=0.9,
        hovertemplate= "%{x|%d %b, '%y %I%M%p}<br><b>%{y}<extra></extra>"
    ))

    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    fig.update_layout(template='plotly_white')

    # fig.show()
    #fig.write_html(f"data/{title_name}_metric_price.html")

    fig.update_layout(
        plot_bgcolor=fill_color,
        paper_bgcolor = "#DCEEF2",
        title={
            "text": f"<span style='font-size:30px;color:{line_color};font-weight:bold;'>{title_name}</span><br>",#<span style='font-size:18px;color:#4C5958;'>{updated_date:%a %b %#d, %Y %H:%M%p}</span>",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font_family': 'Overpass'
    }
    )
    fig.update_layout(
        margin=dict(l=5, r=5, t=5, b=5),
    )

    st.plotly_chart(fig, use_container_width=True)


def fifty_two_high(ticker):

    #fifty_two_week_HIGH, fifty_two_week_LOW, two_hundred_day_AVG, previous_CLOSE, \
    #reg_MARKET, price_change, percent_change= ticker_numbers(ticker=ticker)

    import json
    with open(DATA_DIR) as file:
        contents = file.read()
    parsed_contents = json.loads(contents)

    p_change = ((parsed_contents['fifty_two_HIGH'] - parsed_contents['reg_MARKET'])/parsed_contents['fifty_two_HIGH'])*100


    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=parsed_contents['fifty_two_HIGH'],
        number={"prefix": "$"},
        number_font=dict(size=50, color='#182033'),
        delta={"reference": parsed_contents['reg_MARKET'], "valueformat":".2f", 'relative': False, 'position': 'bottom',
               "suffix": f"({p_change:.2f}%)"},
        # domain = {'x':[1, 1], 'y':[0.5,0]},
        delta_decreasing=dict(color=candle_fall),
        delta_increasing=dict(color=candle_rise),
        delta_font=dict(size=20),
    ))

    fig.update_layout(
                paper_bgcolor="#E5FFEE",
                font_family='Overpass',
                title={
                    "text": "<span style='font-size:20px;color:#182033;'>52 WEEK HIGH</span><br>",
                    'y': 0.9,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'font_family': 'Overpass'
    })

    fig.update_layout(
        margin=dict(l=10, r=10, t=10, b=10),
    )

    st.plotly_chart(fig, use_container_width=True)

def fifty_two_low(ticker):

    #fifty_two_week_HIGH, fifty_two_week_LOW, two_hundred_day_AVG, previous_CLOSE, \
    #reg_MARKET, price_change, percent_change = ticker_numbers(ticker=ticker)

    import json
    with open(DATA_DIR) as file:
        contents = file.read()
    parsed_contents = json.loads(contents)

    p_change = ((parsed_contents['fifty_two_LOW'] - parsed_contents['prev_CLOSE']) / parsed_contents['fifty_two_LOW']) * 100

    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=parsed_contents['fifty_two_LOW'],
        number={"prefix": "$"},
        number_font=dict(size=50, color='#182033'),
        delta={"reference": parsed_contents['prev_CLOSE'], "valueformat": ".2f", 'relative': False,
               "suffix": f"({p_change:.2f}%)"},
        # domain = {'x':[1, 1], 'y':[0.5,0]},
        delta_decreasing=dict(color=candle_fall),
        delta_increasing=dict(color=candle_rise),
        delta_font=dict(size=20)
    ))


    fig.update_layout(paper_bgcolor="#DCEEF2")
    fig.update_layout(
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="#FFE1DE",
        font_family='Overpass',
        title={
            "text": "<span style='font-size:20px;color:#182033;'>52 WEEK LOW</span><br>",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font_family': 'Overpass'}
    )



    st.plotly_chart(fig, use_container_width=True)

def two_hundred_avg(ticker):
    # fifty_two_week_HIGH, fifty_two_week_LOW, two_hundred_day_AVG, previous_CLOSE, \
    # reg_MARKET, price_change, percent_change = ticker_numbers(ticker=ticker)

    import json
    with open(DATA_DIR) as file:
        contents = file.read()
    parsed_contents = json.loads(contents)

    p_change = ((parsed_contents['two_hundred_AVG'] - parsed_contents['prev_CLOSE']) / parsed_contents['prev_CLOSE']) * 100

    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=parsed_contents['two_hundred_AVG'],
        number={"prefix": "$"},
        number_font=dict(size=50, color='#182033'),
        delta={"reference": parsed_contents['prev_CLOSE'], "valueformat": ".2f", 'relative': False,
               "suffix": f"({p_change:.2f}%)"},
        # domain = {'x':[1, 1], 'y':[0.5,0]},
        delta_decreasing=dict(color=candle_fall),
        delta_increasing=dict(color=candle_rise),
        delta_font=dict(size=20),
    ))

    fig.update_layout(paper_bgcolor="#DCEEF2")
    fig.update_layout(
        margin=dict(l=10, r=10, t=10, b=10),
        font_family='Overpass',
        title={
            "text": "<span style='font-size:20px;color:#182033;'>200 DAY AVERAGE</span><br>",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font_family': 'Overpass'}
    )

    st.plotly_chart(fig, use_container_width=True)

