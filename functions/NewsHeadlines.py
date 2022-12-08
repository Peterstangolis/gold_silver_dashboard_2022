
## A function that pulls in the latest news headlines for a particular commodity

def news_headlines(ticker):

    import time
    import pytz
    from pytz import timezone
    import yfinance as yf

    eastern = timezone('US/Eastern')
    fmt = '%b %d, %Y %#I:%M%p %Z'

    data = yf.Ticker(ticker)

    headlines = dict()
    for n in range(len(data.news)):
        key = 'Article' + '_' + str(n)
        title = data.news[n]['title']
        link = data.news[n]['link']
        source = data.news[n]['publisher']

        t = time.strftime(fmt, time.localtime(data.news[n]["providerPublishTime"]))
        article_date_time = t
        try:
            image_link = data.news[n]['thumbnail']['resolutions'][0]['url']
            headlines[key] = [title, link, source, image_link, article_date_time]
        except:
            image_link = ""
            headlines[key] = [title, link, source, image_link, article_date_time]

    return headlines
