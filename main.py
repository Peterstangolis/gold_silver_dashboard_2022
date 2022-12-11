

## Created functions
from functions.UpdatedMetricNums import updated_metric, fifty_two_high, fifty_two_low, two_hundred_avg
from functions.OneDayPlotlyPlot import one_day_plotly_plot
from functions.MaxPlotlyPlot import max_plotly_plot
from functions.NewsHeadlines import news_headlines
from functions.TickerNumbers import ticker_numbers
from variables import *

import streamlit as st
import datetime


## Run the functions


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide",
                   page_title="GOLD & SILVER PRICES",
                   page_icon="🪙")

if "ticket_selected" not in st.session_state:
    st.session_state.ticket_selected = gold

if "chart_type" not in st.session_state:
    st.session_state.chart_type = "ONE DAY"


with st.sidebar:
    with st.form(key="submit_selection"):
        st.selectbox("SELECT TICKER SYMBOL", list(commodities.values()), index=0, key="ticket_selected")
        st.radio('SELECT CHART TYPE', ["ONE DAY", "HISTORY"], horizontal=True, key="chart_type")
        submitted = st.form_submit_button(label="Submit")

    st.write(submitted)

st.markdown(f"<span style='font-color:black;font-size:44px;font-family:arial;font-weight:bold;'>{chart_colours_title[st.session_state.ticket_selected][0]} STATS AND FIGURES </span><span style='font-color:{chart_colours_title[st.session_state.ticket_selected][1]};font-size:24px;font-style:italic;'>({st.session_state.ticket_selected})</span>", unsafe_allow_html=True)

if submitted:

    ## Run function to retrieve latest numbers for selected ticker
    ticker_numbers(ticker=st.session_state.ticket_selected)

    st.markdown(f"LAST UPDATE: {datetime.datetime.today():%A %b %#d, %Y %H:%M}", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([3, 1.5, 1.5, 1.5], gap = 'small')

    # fifty_two_week_HIGH, fifty_two_week_LOW, two_hundred_day_AVG, previous_CLOSE, \
    #     reg_MARKET, price_change, percent_change, updated_date = ticker_numbers(ticker=gold)

    ## TOP 4 COLUMNS OF DATA
    with col1:
        updated_metric(ticker=st.session_state.ticket_selected, title_name=chart_colours_title[st.session_state.ticket_selected][0],
                       line_color=chart_colours_title[st.session_state.ticket_selected][1],
                       fill_color=chart_colours_title[st.session_state.ticket_selected][2])

    with col2:
        fifty_two_high(ticker=st.session_state.ticket_selected)

    with col3:
        fifty_two_low(ticker=st.session_state.ticket_selected)

    with col4:
        two_hundred_avg(ticker=st.session_state.ticket_selected)


    if st.session_state.chart_type == "ONE DAY":
        one_day_plotly_plot(increase_c=candle_rise, decrease_c=candle_fall,
                            volume_c=chart_colours_title[st.session_state.ticket_selected][1], template_p=plotly_template,
                            period=two_day_period if datetime.datetime.today().weekday() == 6 else one_day_period,
                            interval=fifteenMinute_interval,
                            ticker=st.session_state.ticket_selected)

    elif st.session_state.chart_type == "HISTORY":
        max_plotly_plot(increase_c=candle_rise,
                        decrease_c=candle_fall,
                        volume_c=chart_colours_title[st.session_state.ticket_selected][1],
                        fill_color=chart_colours_title[st.session_state.ticket_selected][2],
                        template_p='plotly_white',
                        period=max_period,
                        interval=one_day_period,
                        ticker=st.session_state.ticket_selected
                        )

    with st.sidebar:
        news = news_headlines(ticker=st.session_state.ticket_selected)
        headline_keys = list(news.keys())
        st.markdown("<hr>", unsafe_allow_html=True)
        st.write(f"<span style = 'font-weight:bold;font-size:20px;font-family:liberation serif;color:{chart_colours_title[st.session_state.ticket_selected][1]}'>LATEST HEADLINES FOR {chart_colours_title[st.session_state.ticket_selected][0]}</span>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        for i in range(len(headline_keys)):
            key = headline_keys[i]
            st.write(f"<p style = 'font-size:18px;font-family:liberation serif;color:{chart_colours_title[st.session_state.ticket_selected][3]};'>{news[key][0]}</p>", unsafe_allow_html=True)
            st.markdown(f"<span style = 'color:#0076A9;font-size:12px;'> {news[key][2]} </span> <span style = 'color:{chart_colours_title[st.session_state.ticket_selected][1]};font-size:13px;'> | {news[key][4]} </span> ", unsafe_allow_html=True)
            if len(news[key][3]) > 2:
                #st.image(f'{headlines[key][3]}', width=100)
                image_link = f"<a href='{news[key][1]}'><img src='{news[key][3]}' alt = 'article image' style = 'width:190px;height:120px; border: 2px solid lightgrey;border-radius:10px;'></a>"
                st.markdown(f"{image_link}", unsafe_allow_html=True)
            else:
                website_image = 'https://images.unsplash.com/photo-1523995462485-3d171b5c8fa9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80'
                image_link = f"<a href='{news[key][1]}'><img src= '{website_image}' alt = 'article image' style = 'width:190px;height:120px; border: 2px solid lightgrey;border-radius:10px;'></a>"
                st.markdown(f"{image_link}", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)



else:
    st.image("https://images.pexels.com/photos/8369648/pexels-photo-8369648.jpeg", width=600)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Running")

