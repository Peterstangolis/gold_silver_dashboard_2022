import datetime

## Created functions
from functions.UpdatedMetricNums import updated_metric, fifty_two_high, fifty_two_low, two_hundred_avg
from functions.OneDayPlotlyPlot import one_day_plotly_plot
from functions.NewsHeadlines import news_headlines
from functions.TickerNumbers import ticker_numbers
from variables import *



import streamlit as st
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# import datetime
# import yfinance as yf


## Run the functions


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="GOLD & SILVER PRICES", page_icon="random")

st.title("TESTING")

st.markdown(f"LAST UPDATE: {datetime.datetime.today():%A %b %#d, %Y %H:%M}", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 2], gap = 'small')

# fifty_two_week_HIGH, fifty_two_week_LOW, two_hundred_day_AVG, previous_CLOSE, \
#     reg_MARKET, price_change, percent_change, updated_date = ticker_numbers(ticker=gold)

with col1:
    updated_metric(ticker=gold, title_name=title_gold, line_color=volume_gold)
with col2:
    fifty_two_high(ticker=gold)

with col3:
    fifty_two_low(ticker=gold)

with col4:
    two_hundred_avg(ticker=gold)

with col5:
    news = news_headlines(ticker=gold)
    headline_keys = list(news.keys())
    st.write("NEWS")
    #st.write(news)
    for i in range(len(headline_keys)):
        key = headline_keys[i]
        st.write(f"<p style = 'font-size:18px;font-family:liberation serif;color:black;'>{news[key][0]}</p>", unsafe_allow_html=True)
        st.markdown(f"<span style = 'color:#0076A9;font-size:12px;'> {news[key][2]} </span> <span style = 'color:lightgrey;font-size:13px;'> | {news[key][4]} </span> ", unsafe_allow_html=True)
        if len(news[key][3]) > 2:
            #st.image(f'{headlines[key][3]}', width=100)
            image_link = f"<a href='{news[key][1]}'><img src='{news[key][3]}' alt = 'article image' style = 'width:190px;height:120px; border: 2px solid lightgrey;border-radius:10px;'></a>"
            st.markdown(f"{image_link}", unsafe_allow_html=True)
        else:
            website_image = 'https://images.unsplash.com/photo-1523995462485-3d171b5c8fa9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80'
            image_link = f"<a href='{news[key][1]}'><img src= '{website_image}' alt = 'article image' style = 'width:190px;height:120px; border: 2px solid lightgrey;border-radius:10px;'></a>"
            st.markdown(f"{image_link}", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)


one_day_plotly_plot(increase_c=candle_rise , decrease_c=candle_fall, volume_c=volume_gold, template_p = plotly_template, period = one_day_interval, interval = fifteenMinute_interval, ticker = gold)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Running")

