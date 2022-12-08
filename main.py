
## Created functions
from functions.UpdatedMetricNums import updated_metric
from variables import *



import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime


## Run the functions
updated_metric(ticker=gold, title_name=title_gold, line_color=volume_gold)


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="GOLD & SILVER PRICES", page_icon="🪙")

st.title("TESTING")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Running")

