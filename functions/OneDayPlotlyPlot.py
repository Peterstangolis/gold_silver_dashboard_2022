
## A function that takes in data from a commodity for one day and returns a Plotly Candlestick plot

from functions.OneDayData import one_day_data
from variables import plotly_template

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import streamlit as st

def one_day_plotly_plot(increase_c, decrease_c, volume_c, template_p, period, interval, ticker):
    last_updated, last_price, one_day_prices = one_day_data(period=period, interval=interval, ticker=ticker)

    fig_ticker = make_subplots(rows=2, cols=1, shared_xaxes=True,vertical_spacing=0.01,row_heights=[0.7, 0.3])

    fig_ticker.add_trace(go.Candlestick(x=one_day_prices.index,
                                        open=one_day_prices["Open"],
                                        high=one_day_prices["High"],
                                        low=one_day_prices["Low"],
                                        close=one_day_prices["Close"],
                                        whiskerwidth=.5,
                                        increasing_line_color='#00B250',
                                        decreasing_line_color='#B21102',
                                        showlegend=False,
                                        # hovertemplate="%{x}, %{open}, %{high}, %{low}, %{close} <extra></extra>"
                                        ),
                         row=1, col=1)

    fig_ticker.update_xaxes(showspikes=True,
                            # spikecolor='yellow',
                            spikedash='longdash',
                            spikethickness=1.1,
                            spikesnap='cursor'
                            )

    fig_ticker.update_yaxes(showspikes=True,
                            side='right',
                            tickformat='.2f',
                            spikedash='longdash',
                            spikethickness=1.1,
                            spikemode='across',
                            row=1, col=1)

    fig_ticker.add_hline(y=last_price,
                         line_dash='dash',
                         line_width=0.5,
                         opacity=1.0,
                         line_color=volume_c,
                         annotation_text=f"Last Close Price {ticker}",
                         annotation_position="top left",
                         annotation=dict(font_size=12, font_family="Arial", font_color=volume_c),
                         row=1, col=1),

    fig_ticker.add_trace(go.Bar(x=one_day_prices.index,
                                y=one_day_prices.Volume,
                                marker_color=volume_c,
                                opacity=1.0,
                                hovertemplate="%{x},<br><b> %{y} <extra></extra>"
                                ),
                         row=2, col=1)

    # Last Price
    fig_ticker.add_annotation(xref="paper",
                              yref="y",
                              x=1.06,
                              y=f"{last_price:.3f}",
                              text=f"<b>{last_price:.3f}",
                              showarrow=False,
                              font=dict(
                                  family="Arial, monospace",
                                  size=12.5,
                                  color='white'),
                              borderpad=1,
                              bordercolor=None,
                              borderwidth=1,
                              bgcolor=volume_c,
                              opacity=0.9
                              )

    # Last Updated
    fig_ticker.add_annotation(xref="paper",
                              yref="paper",
                              x=1,
                              y=1.1,
                              text=f"LAST UPDATE: <b>{last_updated:%b %#d, %Y %H:%M}",
                              showarrow=False,
                              font=dict(
                                  family="Arial, monospace",
                                  size=12,
                                  color='black'),
                              borderpad=3,
                              bordercolor=None,
                              borderwidth=1,
                              bgcolor=None,
                              opacity=0.9
                              )

    fig_ticker.update_layout(xaxis_rangeslider_visible=False,
                             showlegend=False,
                             height=600,
                             width=1000,
                             template=plotly_template,
                             spikedistance=1000, hoverdistance=100)

    st.plotly_chart(fig_ticker, use_container_width=True)