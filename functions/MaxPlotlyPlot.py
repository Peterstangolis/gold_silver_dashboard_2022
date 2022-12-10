
## A function that takes in the max data available for a commodity and returns a plotly line chart
from functions.MaxTickerData import max_ticker_data

import plotly.graph_objects as go
import streamlit as st


def max_plotly_plot(increase_c, decrease_c, volume_c, fill_color, template_p, period, interval, ticker):

    import streamlit as st

    last_updated, last_price, max_prices = max_ticker_data(period=period, interval=interval, ticker=ticker)

    trace1 = go.Scatter(
        name='Close',
        x=max_prices.index,
        y=max_prices["Close"],
        mode='lines',
        line=dict(color=volume_c),
        fillcolor=fill_color,
        fill='tonexty')

    data = [trace1]

    layout = go.Layout(
        yaxis=dict(title='Price'),
        #title=f'{ticker} Volatility Visualization',
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(count=5, label="5y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            rangebreaks=[
                dict(bounds=["sat", "sun"])
            ],
            type='date'

        ),
        showlegend=False,
        height=600,
        width=1000,
        template=template_p
    )

    fig_ticker = go.Figure(data=data, layout=layout)

    fig_ticker.update_yaxes(
        showspikes=True,
        side='right',
        tickformat='.3f',
        spikedash='longdash',
        spikethickness=.8
    )

    fig_ticker.add_annotation(xref="paper",
                              yref="y",
                              x=1.05,
                              y=f"{last_price:.3f}",
                              text=f"<b>{last_price:.3f}",
                              showarrow=False,
                              font=dict(
                                  family="Arial, monospace",
                                  size=13,
                                  color="#DEEFE7"),
                              borderpad=3,
                              bordercolor='#FF867A',
                              borderwidth=1,
                              bgcolor='#FF1A05',
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

    fig_ticker.update_layout(
        margin=dict(l=10, r=10, t=10, b=10)
    )

    st.plotly_chart(fig_ticker, use_container_width=True)