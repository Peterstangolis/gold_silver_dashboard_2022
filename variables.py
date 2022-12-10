
## Variables used throughout the dashboard

# TICKERS
gold = "GC=F"
silver = "SI=F"
tsx = "^GSPTSE"


title_silver = "SILVER"
title_gold = "GOLD"
title_tsx = "TSX"

commodities = {
    title_gold:gold,
    title_silver:silver,
    title_tsx:tsx
}


one_day_period = '1d'
max_period = 'max'
fifteenMinute_interval = '15m'
fiveMinute_interval = '5m'
one_day_interval = '1d'


# COLORS:
candle_rise = '#00B250'
candle_fall = '#B21102'
volume_silver = '#B4BEC9'
fill_color_silver = '#F2F2F2'
volume_gold =  '#A67926'
fill_color_gold = 'rgba(255, 186, 59, 0.2)'
volume_tsx = '#6986B3',
fill_color_tsx = '#B0D0FF'

# CHART COLOURS:
chart_colours_title = {
    gold: [title_gold, volume_gold, fill_color_gold],
    silver: [title_silver, volume_silver, fill_color_silver],
    tsx: [title_tsx, volume_tsx, fill_color_tsx]
}

## Plotly Template
plotly_template = 'plotly_white'